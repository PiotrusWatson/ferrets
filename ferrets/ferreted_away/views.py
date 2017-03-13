from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    context_dict = {'stuff':'place holder stuff'}
    return render(request, 'ferrets/index.html', context_dict)


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
    return render(request, "ferrets/login.html")

def addAccount(request):
    return render(request, "ferrets/addaccount.html")

#@login_required
def myAccount(request):
    return render(request, "ferrets/myaccount.html")

#@login_required
def myItems(request):
    return render(request, "ferrets/myitems.html")

#@login_required
def addItems(request):
    return render(request, "ferrets/additems.html")

#@login_required
def myWatchlist(request):
    return render(request, "ferrets/mywatchlist.html")
def categories(request):
    return render(request, "ferrets/categories.html")

def showCategory(request):
    return render(request, "ferrets/showcategory.html")

def showItem(request):
    return render(request, "ferrets/showitem.html")