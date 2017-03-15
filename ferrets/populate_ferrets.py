import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ferrets.settings')

import django
django.setup()

from django.contrib.auth.models import User
from ferreted_away.models import Category, Item, UserProfile

def populate():
    #basic user
    sample_user = {"user": "fredrick",
         "email": "fredricksemail@gmail.com",
         "password": "fred123rick"}

    #items
    transport_items = [
        {"item_name": "Rollerskates",
         "price": "20.00",
         "description": "Neon pink rollerskates, size 6."},
        {"item_name": "Private Jet",
         "price": "24000.00",
         "description": "Small turboprop jet. Airport not included."},
        {"item_name": "VW Golf",
         "price": "5.00",
         "description": "Not a real VW Golf, just a toy one."},
        {"item_name": "Vespa Moped",
         "price": "145.00",
         "description": "Small red moped, slight scrape above rear wheel due to failed wheelie attempt."}]

    accomodation_items = [
        {"item_name": "Room in 2 Bed Flat",
         "price": "450.00",
         "description": "Near Viper, Great Western Road. Bills not included."},
        {"item_name": "Penthouse Apartment",
         "price": "2000.00",
         "description": "Views of the clyde, very high up, 20th floor apartment."},
        {"item_name": "Batcave",
         "price": "1300.00",
         "description": "Some issues with damp, comes with own Batmobile."}]

    food_items = [
        {"item_name": "Tefal Frying Pan",
         "price": "10.00",
         "description": "24 cm frying pan,good condition, other brands are available."},
        {"item_name": "Leftover Curry",
         "price": "3.50",
         "description": "4 portions of leftover vegetable curry, will keep in refrigerator for 3 days."},
        {"item_name": "Pear and Banana",
         "price": "2.00",
         "description": "Ripe so ready to eat, willing to sell seperately by arrangement."}]

    clothes_items = [
        {"item_name": "Levi Jeans",
         "price": "70.00",
         "description": "High waisted skinny jeans in dark blue acid wash."},
        {"item_name": "Gucci Handbag",
         "price": "675.00",
         "description": "Black and red leather handbag. One careful owner."},
        {"item_name": "Nike Running Shoes",
         "price": "45.00",
         "description": "Purple running trainers with yellow laces. Good for cross country running, grippy soles."},
        {"item_name": "Blue T-shirt",
         "price": "12.00",
         "description": "Blue GUTS t-shirt with CDX 2017 logo. Brand new, never been worn."}]

    books_items = [
        {"item_name": "Guide to Databases",
         "price": "40.00",
         "description": "Latest course textbook for CS1Q databases course"},
        {"item_name": "The Catcher in the Rye",
         "price": "2.70",
         "description": "Couldn't finish it, narrator too pretentious."},
        {"item_name": "Maths 1R Textbook",
         "price": "13.00",
         "description": "Book valued at a tenner but charging an extra 3 for my helpful annotations in the margins."},
        {"item_name": "Complete Divergent Series",
         "price": "24.00",
         "description": "Really good series, but just not as good as the films."}]

    other_items = [
        {"item_name": "Box of Fireworks",
         "price": "120.00",
         "description": "Mostly sparklers, but a few rockets and catherine wheels too."},
        {"item_name": "Golf Clubs",
         "price": "370.00",
         "description": "Complete set of golf clubs with bag, and a set of golf balls."},
        {"item_name": "Laptop",
         "price": "500.00",
         "description": "Selling as was gifted a macbook for christmas so no longer need this. Fast little machine."}]

    #categories
    cats = {"Transport": {"items": transport_items},
            "Accomodation": {"items": accomodation_items},
            "Food": {"items": food_items},
            "Clothes": {"items": clothes_items},
            "Books": {"items": books_items},
            "Other": {"items": other_items}}

    #adds all the stuff above to the database
    
    up = add_user(sample_user)
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for i in cat_data["items"]:
            add_item(c, up, i["item_name"], i["price"], i["description"])

    for c in Category.objects.all():
        for i in Item.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(i)))

def add_user(sample_user):
    u.set_password(sample_user["password"])
    u.save()
    up = UserProfile.objects.get_or_create(user=u, email=sample_user["email"])
    up.save()
    return up

def add_item(cat, user, name, price, description, views=0):
    i = Item.objects.get_or_create(category=cat, item_name=name)[0]
    i.price=price
    i.description=description
    i.views=views
    i.save()
    return i

def add_cat(name):
    c = Category.objects.get_or_create(name=name)
    c.save()
    return c

if __name__ == '__main__':
    print("Starting ferreted_away population script...")
    populate()




