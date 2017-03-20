from django import forms
from django.contrib.auth.models import User
from ferreted_away.models import Category, Item, UserProfile, Comments
import datetime

class ItemForm(forms.ModelForm):

    item_name = forms.CharField(max_length=128,
                           help_text="Please insert the item name.")
    price = forms.DecimalField(initial=0)
    description = forms.CharField(max_length=350,
                                  help_text="Please insert a Description")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    picture = forms.ImageField
    



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
    picture = forms.ImageField
    class Meta:
        model = UserProfile
        fields = ('picture',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        exclude = ('user','item',)
        fields = ('comment',)
