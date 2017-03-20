from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

import random

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    itemId = models.IntegerField(unique=True)
    item_name = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=21, decimal_places=2)
    description = models.TextField(max_length=350, blank=True)
    picture = models.ImageField(upload_to="uploads/", default="other/placeholder.png", blank=True)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            self.itemId = random.randint(0,1000000)
        except:
            save(self, *args, **kwargs)
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.item_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', default="other/placeholder.png", blank=True)

    def __str__(self):
        return self.user.username

class Watchlist(models.Model):
    user = models.ForeignKey(User)
    item = models.IntegerField(blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

class Comments(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    comment = models.TextField(max_length=360, blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Comments'

