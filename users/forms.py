from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import About,Event


class UserRegistrationForm (UserCreationForm):
    email = forms.EmailField()

    #namespace to declare what this form targets
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']


class AboutUsUpdateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['content']


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','image','content']