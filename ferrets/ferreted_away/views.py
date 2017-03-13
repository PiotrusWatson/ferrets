from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def home(request):
    context_dict = {'stuff':'place holder stuff'}
    return render(request, 'ferrets/index.html', context_dict)


def about(request):
    context_dict = {'stuff':'place holder stuff'}
    return render(request, 'ferrets/about.html', context_dict)



def faq(request):
    return HttpResponse("FAQ")

def contact(request):
    return HttpResponse("Contact")

def sitemap(request):
    return HttpResponse("Sitemap")

def login(request):
    return HttpResponse("Login")

def addAccount(request):
    return HttpResponse("Add Account")

def myAccount(request):
    return HttpResponse("My Account")

def myItems(request):
    return HttpResponse("My Items")

def addItems(request):
    return HttpResponse("Add Items")

def myWatchlist(request):
    return HttpResponse("My Watchlist")

def categories(request):
    return HttpResponse("Categories")

def showCategory(request):
    return HttpResponse("Show Category")

def showItem(request):
    return HttpResponse("Show Item")