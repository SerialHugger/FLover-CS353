
from django import forms
from theApp.models import *
#from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    USERTYPES = [('1','Customer'), ('2','Seller'), ('3','Courier')]
    password = forms.CharField(widget=forms.PasswordInput())
    userType = forms.CharField(label = 'Choose a user type', widget = forms.Select(choices=USERTYPES))
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta():
        model = myUser
        fields = ('username','password','email','userType')

class flowerForm(forms.ModelForm):
    flower_type = forms.CharField(max_length=100)
    color = forms.CharField(max_length=100)
    occasion = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    FLOWERCATEGORIES = [('1','plastic'), ('2','focal'), ('3','filler'), ('4', 'line')]
    category = forms.CharField(label = 'Choose a category', widget = forms.Select(choices=FLOWERCATEGORIES))
    class Meta():
        model = Flower
        fields = ('flower_type','color','occasion','price','stock_count','photo_id','description','category')

class gizliForm(forms.ModelForm):
    
    class Meta():
        model = Category
        fields = ('name',)
        
class deletionForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    class Meta():
        model = Flower
        fields = ('name',)

class updatePriceForm(forms.ModelForm):
    flower_type = forms.CharField(max_length=100)
    class Meta():
        model = Flower
        fields = ('flower_type','price')