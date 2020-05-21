
from django import forms
from theApp.models import *
#from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = myUser
        fields = ('username','password','email','userType')

class flowerForm(forms.ModelForm):
    
    class Meta():
        model = Flower
        fields = ('flower_type','color','occasion','price','stock_count','photo_id','description','category')

class gizliForm(forms.ModelForm):
    
    class Meta():
        model = Category
        fields = ('name',)