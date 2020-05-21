
from django import forms
from theApp.models import myUser
#from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = myUser
        fields = ('username','password','email','userType')