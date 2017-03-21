from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from ferreted_away.models import Category, Item, UserProfile, Watchlist, Comments
from ferreted_away.forms import UserForm, UserProfileForm, CommentForm, ItemForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail, BadHeaderError
from decimal import Decimal
from django.contrib import messages

def home(request):
    item_list = Item.objects.order_by('-views')[:3] #3 of the most viewed items

    context_dict = {'items': item_list,
                    }
    #if user is logged in, show watchlist
    if request.user.is_authenticated():

        #get all item ids from the watchlist linked to the user and ordered by most recently added
        item_ids = Watchlist.objects.filter(user=request.user).order_by("-date_added").values_list('item')
        #use this to get the last 3 items added to the watchlist
        watched_list = Item.objects.filter(itemId__in=item_ids)[:3]
        #add watchlist to the context dict
        context_dict = {'items': item_list,
                        'watched': watched_list,
                        }

    return render(request, 'ferrets/home.html', context=context_dict)

def searchresults(request):
    return render(request, 'ferrets/searchresults.html')

def verify(request):
    return render(request, 'ferrets/google695f0a9a1e7dc6ba.html')

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
        #logging user in
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
        #if the user's account works, take them home
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
        #otherwise, take them to the tragic rejection page :(
            else:
                return HttpResponse("Your account is disabled")
        #if login fails, tell them that :(
        else:
            print("Invalid login details: {0}, {1}".format(username, password))

            return render(request, 'ferrets/login.html', {'message': "Invalid Username or Password"})

    else:
        return render(request, "ferrets/login.html", context_dict)


def addAccount(request):
    registered = False #uses this in the template

    if request.method == 'POST':
        #get image and details from forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #if both forms are good, save the data on them to a new instance of user model
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            #if an image is found in the great aether, saves it as the user's image
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
    #shows last 5 items and watchlist items added
    my_items = Item.objects.filter(user=request.user).order_by("-date_added")[:5]

    item_ids = Watchlist.objects.filter(user=request.user).order_by("-date_added").values_list('item')

    my_watchlist = Item.objects.filter(itemId__in=item_ids)[:5]

    context_dict = {"my_items": my_items, "my_watchlist": my_watchlist, "user": request.user}
    return render(request, "ferrets/myaccount.html", context_dict)


@login_required
def myItems(request):
    items = Item.objects.filter(user=request.user)
	
    context_dict = {"my_items": items,
                    }
    return render(request, "ferrets/myItems.html", context_dict)


@login_required
def addItems(request, username):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            if username:
                item = form.save(commit=False)
                item.user = request.user

                if 'picture' in request.FILES:
                    item.picture = request.FILES['picture']

                item.save()

                return HttpResponseRedirect(reverse('myItems'))
    else:
        print(form.errors)
    context_dict = {'form': form}
    return render(request, 'ferrets/addItems.html', context_dict)


@login_required
def myWatchlist(request):
    #shows last watchlist items added
    item_ids = Watchlist.objects.filter(user=request.user).order_by("-date_added").values_list('item')

    my_watchlist = Item.objects.filter(itemId__in = item_ids)




    context_dict = {"watchlist": my_watchlist,
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

    #if an item with specified id does exist
    try:
        item = Item.objects.get(itemId=item_itemId)
        #handling comment posting
        if request.method == 'POST':
            commentForm = CommentForm(data=request.POST)

            if commentForm.is_valid():
                comment = commentForm.save(commit=False)

                comment.user = request.user
                comment.item = item
                comment.save()

            else:
                print(commentForm.errors)
        #assume we are not seller
        context_dict['seller'] = False
        commentForm = CommentForm()

        item.views = item.views + 1
        #if logged in, modify comments based on specific things
        if request.user.is_authenticated:

            logged_in = True
            #displaying comments
            if request.user == item.user:
                context_dict['seller'] = True
                comments = Comments.objects.filter(item=item).order_by('date_added')
            else:
                comments = Comments.objects.filter(item=item, user__in=[item.user, request.user]).order_by(
                        'date_added')

        else:

            logged_in = False

            comments = Comments.objects.filter(item=item, user=item.user).order_by('date_added')

        context_dict['item'] = item


        context_dict['sellUser'] = UserProfile.objects.get(user=item.user)

        context_dict['comments'] = comments

        context_dict['logged'] = logged_in

        context_dict['commentForm'] = commentForm

        context_dict['inWatchlist'] = False

        #try getting current item from watchlist, set bool to true if it finds it
        if request.user.is_authenticated:
            try:
                Watchlist.objects.filter(user=request.user).get(item=item_itemId)
                context_dict['inWatchlist'] = True
            except:
                context_dict['inWatchlist'] = False


    #if item with specified id does not exist, don't fill out anything in the context dict
    except Item.DoesNotExist:

        context_dict['item'] = None

        context_dict['comments'] = None

    return render(request, "ferrets/showitem.html", context_dict)

@login_required
def deleteItem(request, item_itemid):
    try:
        #get item with specified id
        item = Item.objects.get(itemId=item_itemid)

        if request.user.is_authenticated:
            #if user's logged in and it's their item, delete it
            if request.user == item.user:
                item.delete()

        return HttpResponseRedirect(reverse('myItems'))


    except Item.DoesNotExist:

        return HttpResponseRedirect(reverse('myItems'))

@login_required
def addWatchlist(request, item_itemid):
    try:

        item = Item.objects.get(itemId=item_itemid) #look for item

        if request.user.is_authenticated: #if user's logged in, add item to watchlist
            w = Watchlist(item=item_itemid, user=request.user)
            w.save()

        return HttpResponseRedirect(reverse('showItem',args=(item_itemid,)))

    except Item.DoesNotExist: #if item's not, get outta there :)

        return HttpResponseRedirect(reverse('myAccount'))


@login_required
def removeWatchlist(request, item_itemid):
    try: #if an item is found

        item = Item.objects.get(itemId=item_itemid)

        if request.user.is_authenticated: #if user's logged in, get the specified item in watchlist
            watchlist = Watchlist.objects.filter(user=request.user).get(item=item_itemid)

            if watchlist: #if it finds it, delete
                watchlist.delete()

        #redirect to the item's page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('showItem', args=(item_itemid,))))

    except Item.DoesNotExist:
        return HttpResponseRedirect(reverse('myAccount'))

