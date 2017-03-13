from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "ferrets/home.html")


def about(request):
    return render(request, "ferrets/about2.html")


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