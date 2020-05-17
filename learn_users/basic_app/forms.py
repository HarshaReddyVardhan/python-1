from django import forms
from basic_app.models import userProfileInfo
from django.contrib.auth.models import User

class userForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class userProfileForm(forms.ModelForm):

    class Meta():
        model = userProfileInfo
        fields = ('protofolio_site','profile_pic')
