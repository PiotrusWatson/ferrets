from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
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
    item_name = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=21, decimal_places=2)
    description = models.TextField(max_length=350, blank=True)
    picture = models.ImageField(upload_to='item_images', blank=True)
    views = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.item_name

class User(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=254, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Watchlist(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)

class Comments(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    comment = models.TextField(max_length=360, blank=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = 'Comments'
