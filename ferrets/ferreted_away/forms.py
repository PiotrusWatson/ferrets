from django import forms
from django.contrib.auth.models import User
from ferreted_away.models import Category, Item, UserProfile
from datetime import datetime

class ItemForm(forms.ModelForm):

    item_name = forms.CharField(max_length=128,
                           help_text="Please insert the item name.")
    price = forms.DecimalField(initial=0)
##    description = forms.TextField(max_length=350,
                                  ##help_text="Please insert a Description")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    date_added = forms.DateField(widget=forms.HiddenInput(), initial=datetime.now())

##    category = models.ForeignKey(Category)
##    picture = models.ImageField(upload_to='item_images', blank=True)

    class Meta:
        model = Item
        exclude = ('user',)
        fields = ('category','item_name','price','description','picture' )



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('picture')

