from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render
from ferreted_away.models import Category, Item, User, Watchlist
from ferreted_away.forms import UserForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

def home(request):
    item_list = Item.objects.order_by('-views')[:5]


    context_dict = {'items': item_list,
                    }

    if request.user.is_authenticated():
        watched_list = Watchlist.filter(user=request.user.user).order_by("-date_added")[:5]
        context_dict = {'items': item_list,
                        'watched': watched_list,
                        }

    return render(request, 'ferrets/home.html', context=context_dict)


def about(request):
    context_dict = {'stuff':'place holder stuff'}
    return render(request, 'ferrets/about.html', context_dict)

def faq(request):
    return render(request, "ferrets/faq.html")

def contact(request):
    return render(request, "ferrets/contact.html")

def sitemap(request):
    return render(request, "ferrets/sitemap.html")


def login(request):

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your Rango account is disabled")

        else:
            print("Invalid login details: {0}, {1}".format(username, password))

            return render(request, 'ferrets/login.html',{'message' :"Invalid Username or Password"})

    else:
        return render(request, "ferrets/login.html", {})

def addAccount(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            if 'picture' in request.FILES:
                user.picture = request.FILES['picture']

            user.save()

            registered = True
            return HttpResponseRedirect(reverse('myAccount'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'ferrets/addaccount.html', {'user_form': user_form,
                                                   'registered': registered})


@login_required
def myAccount(request):
    my_items = Item.objects.filter(user=request.user.user).order_by("-date_added")[:5]
    my_watchlist = Watchlist.filter(user=request.user.user).order_by("-date_added")[:5]

    context_dict = {"my_items":my_items, "my_watchlist":my_watchlist}
    return render(request, "ferrets/myaccount.html", context_dict)

@login_required
def myItems(request):
    items = Item.objects.filter(user=request.user.user)

    context_dict = {"items": items}
    return render(request, "ferrets/myitems.html", context_dict)

@login_required
def addItems(request):
    return render(request, "ferrets/additems.html")

@login_required
def myWatchlist(request):
    watchlist = Watchlist.filter(user=request.user.user).order_by("-date_added")[:5]

    context_dict = {"watchlist": watchlist}
    return render(request, "ferrets/mywatchlist.html", context_dict)

def categories(request):
    categories = Category.objects

    context_dict ={"categories": categories}

    return render(request, "ferrets/categories.html", context_dict)

def showCategory(request):
    return render(request, "ferrets/showcategory.html")

def showItem(request):
    return render(request, "ferrets/showitem.html")