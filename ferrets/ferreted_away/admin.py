from django.contrib import admin
from ferreted_away.models import Category, Item, Watchlist, Comments

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Watchlist)
admin.site.register(Comments)

# Register your models here.
