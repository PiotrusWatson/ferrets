from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from ferreted_away.models import Category, Item, UserProfile, Watchlist, Comments
from ferreted_away.forms import UserForm, UserProfileForm, CommentForm, ItemForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from decimal import Decimal


def home(request):
    item_list = Item.objects.order_by('-views')[:3]

    context_dict = {'items': item_list,
                    }

    if request.user.is_authenticated():
        watched_list = Watchlist.objects.filter(user=request.user)
        watched_list = watched_list.order_by("-date_added")[:3]
        context_dict = {'items': item_list,
                        'watched': watched_list,
                        }

    return render(request, 'ferrets/home.html', context=context_dict)


def about(request):
    return render(request, 'ferrets/about.html')


def faq(request):
    return render(request, "ferrets/faq.html")


def contact(request):
    return render(request, "ferrets/contact.html")


def sitemap(request):
    return render(request, "ferrets/sitemap.html")


def user_login(request):
    context_dict = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Rango account is disabled")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))

            return render(request, 'ferrets/login.html', {'message': "Invalid Username or Password"})

    else:
        return render(request, "ferrets/login.html", context_dict)


def addAccount(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'ferrets/addaccount.html', {'user_form': user_form,
                                                       'profile_form': profile_form,
                                                       'registered': registered,
                                                       })


@login_required
def myAccount(request):
    my_items = Item.objects.filter(user=request.user).order_by("-date_added")[:5]
    my_watchlist = Watchlist.objects.filter(user=request.user).order_by("-date_added")[:5]

    context_dict = {"my_items": my_items, "my_watchlist": my_watchlist, "user": request.user}
    return render(request, "ferrets/myaccount.html", context_dict)


@login_required
def myItems(request):
    items = Item.objects.filter(user=request.user)
	
    context_dict = {"my_items": items,
                    }
    return render(request, "ferrets/myitems.html", context_dict)


@login_required
def addItems(request, username):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            if username:
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return render(request, "ferrets/addItems.html")
    else:
        print(form.errors)
    context_dict = {'form': form}
    return render(request, 'ferrets/addItems.html', context_dict)


@login_required
def myWatchlist(request):
    watchlist = Watchlist.objects.filter(user=request.user).order_by("-date_added")[:5]

    context_dict = {"watchlist": watchlist,
                    }
    return render(request, "ferrets/mywatchlist.html", context_dict)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def categories(request):
    context_dict = {'categories': Category.objects.all(),}

    return render(request, "ferrets/categories.html", context_dict)


def showCategory(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        items = Item.objects.filter(category=category).order_by('-views')

        context_dict['items'] = items

        context_dict['category'] = category

    except Category.DoesNotExist:

        context_dict['category'] = None
        context_dict['items'] = None

    return render(request, 'ferrets/showCategory.html', context_dict)

def browsePrice(request):
    return render(request, 'ferrets/browsePrice.html')

def priceRange(request, priceRange):
    context_dict = {}
    context_dict["range"] = priceRange
    context_dict["items"] = Item.objects.all()
    return render(request, 'ferrets/priceRange.html', context_dict)

## To implement
def showItem(request, item_itemId):
    context_dict = {}

    try:
        item = Item.objects.get(itemId=item_itemId)

        if request.method == 'POST':
            commentForm = CommentForm(data=request.POST)

            if commentForm.is_valid():
                comment = commentForm.save()

                comment.user = request.user
                comment.item = item
                comment.save()

            else:
                print(commentForm.errors)
        else:

            commentForm = CommentForm()

            item.views = item.views + 1

            if request.user.is_authenticated:

                logged_in = True

                if request.user.username == item.user:
                    comments = Comments.objects.filter(item=item).order_by('date_added')
                else:
                    comments = Comments.objects.filter(item=item, user__in=[item.user, request.user.username]).order_by(
                        'date_added')

            else:

                logged_in = False

                comments = Comments.objects.filter(item=item, user=item.user).order_by('date_added')

            context_dict['item'] = item

            context_dict['comments'] = comments

            context_dict['logged'] = logged_in

            context_dict['commentForm'] = commentForm


    except Item.DoesNotExist:

        context_dict['item'] = None

        context_dict['comments'] = None

    return render(request, "ferrets/showitem.html", context_dict)


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        print(request.POST)
        message = request.POST.get("message", None)
        email = request.POST.get("email", None)
        name = request.POST.get("name", None)
        send_mail(
            'FerretedAway Contact Form',
            'Message: ' + message + "\n\nReply e-mail: " + email,
            'ferretedawayteam@gmail.com',
            ['ferretedawayteam@gmail.com'],
            fail_silently=True,
        )
        return HttpResponse("success")
    else:
        return HttpResponse("failure")
