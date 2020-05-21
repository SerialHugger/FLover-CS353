from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from theApp.forms import UserForm
from theApp.models import myUser
from django.db import connection

currentUser = "empty"
cursor = connection.cursor()

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('theApp:index'))

def register(request):
    
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            dataDic = user_form.cleaned_data
            print(dataDic)
            myUser.save(dataDic)
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cursor.execute('Select password, id From theApp_myuser WHERE username = %s', [username])
        tmpTup = cursor.fetchall()[0]
        tmp = tmpTup[0]
        tmpid = tmpTup[1]
        if(password == tmp):
            print('success')
            global currentUser 
            currentUser = tmpid
            return HttpResponseRedirect(reverse('theApp:index'))
        else:
            return HttpResponse("Your account was inactive.")
        '''
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('theApp:index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
        '''
    else:
        return render(request, 'login.html', {})

'''
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
'''
def index(request):
    global currentUser
    curr = currentUser
    print(curr)
    profile_name = "todo" # from profile user alma bakilacak
    most_sold = "todo" # from stocks
    flowers = "todo" # butun flowerlar Select * From Flowers
    # make magic
    print(request.user.username)
    random_flowers = "todo"
    categories = "todo" # get all categories
    context = {"profile_name": profile_name, "most_sold": most_sold} # todo
    return render(request, 'index.html', context)

def seller(request, pk):
    profile_name = "todo" # from profile user alma bakilacak
    products = "todo" # get products from stocks
    seller = "todo" # get seller with pk
    categories = "todo" # get all categories
    context = {"products": products, "seller": seller} # todo
    return render(request, 'seller.html', context)
    
def product(request, pk):
    profile_name = "todo" # from profile user alma bakilacak
    favorite_flowers = "todo" # from profile get favorited
    flower = "todo" # specific flower with pk
    stock = "todo" # get flower stock
    context = {"flower": flower} # todo
    return render(request, 'product.html', context)

def profile(request):
    profile = "todo" # get profile
    orders = "todo" # get orders
    favorites = "todo" # get favorite flowers from fav
    complaint = "todo" # get all complaints with user id
    context = {"temp": temp}
    return render(request, 'profile.html', context)

def contact(request):
    return render(request, 'contact.html')

def contact(request):
    return render(request, 'aboutus.html')

def order(request, pks):
    # pks is a list
    stocks = "todo" # get stocks of flowers
    chocolate = "todo" # get chocolate
    context = {"temp": temp}
    return render(request, 'order.html')

def loginSign(request):
    return render(request, 'login.html')

def changePassword(requst):
    return render(request, 'changePass.html')

def forum(request):
    forumTopics = "todo" # get from forum topics table
    forumCategories = "todo" # get categories from forum categories
    context = {"temp": temp}
    return render(request, 'forum.html')

def postEntry(request, pk):
    forumTopic = "todo" 
    context = {'forumTopic': formTopic}
    return render(request, 'postEntry.html',context)

def forumTopic(request, pk):
    forumTopic = "todo" # get topic with pk
    entries = "todo" #from forumEntry table
    context = {'forumTopic': formTopic}
    return render(request, 'forumTopic.html', context)

def createTopic(request):
    forumCategories = "todo"
    context = {'forumCategories': forumCategories}
    return render(request, 'createTopic.html', context)

def addFlover(request):
    return render(request, 'addFlower.html', context)

def myOrders(request):
    orders = "todo" # Get orders from order delivery
    flower = "todo" # get all flowers
    # then select from orders
    # do this 
    context = {"temp": temp}
    return render(request, 'myOrders.html', context)

def customerService(request):
    cancer = "todo" # get cancer from complaint Report
    username = "todo" # get username with user id from cancer
    context = {"temp": temp}
    return render(request, 'customerService.html', context)

def customerReport(request, pk):
    #using pk get info
    
    return render(request, 'customerReport.html', context)


# Create your views here.
