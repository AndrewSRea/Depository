from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    city = forms.CharField(max_length=100)
    state = forms.CharField(required=False, max_length=50)
    country = forms.CharField(label='Country (if outside U.S.)', required=False, max_length=100)
    favorite_artists = forms.CharField(label='Your favorite artists (use commas)', required=False, max_length=100)
    about_user = forms.CharField(widget=forms.Textarea(attrs={"rows": 7}), label='A small description of yourself', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'city', 'state', 'country', 'favorite_artists', 'about_user']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User 
#         fields = ['username', 'email']


# class ProfileUpdateForm(forms.ModelForm):
#     city = forms.CharField(label='City', max_length=100)
#     state = forms.CharField(label='State', required=False, max_length=50)
#     country = forms.CharField(label='Country (if outside U.S.)', required=False, max_length=100)
#     favorite_artists = forms.CharField(label='Your favorite artists (use commas)', required=False, max_length=200)
#     about_user = forms.CharField(widget=forms.Textarea(attrs={"rows": 7}), label='A small description of yourself', required=False)

#     class Meta:
#         model = Profile
#         fields = ['city', 'state', 'country', 'favorite_artists', 'about_user']