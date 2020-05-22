from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from itertools import chain
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from theApp.forms import *
from theApp.models import *
from django.db import connection
from django.template.defaulttags import register
import random

currentUser = "empty"
cursor = connection.cursor()

'''
@register.filter
def editLink(link):
    return str(link).replace("/product/","theApp/static/uploaded/") + ".jpg"
'''

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
        try:
            tmpTup = cursor.fetchall()[0]
        except:
            return HttpResponse("No such account.")
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

def registerProduct(request):
    registered = False
    if request.method == 'POST':
        flower_form = flowerForm(data=request.POST)
        if flower_form.is_valid():
            dataDic = flower_form.cleaned_data
            print(dataDic)
            fid = Flower.save(dataDic)
            stockDic = {}
            stockDic['flower_id'] = str(fid)
            stockDic['seller_id'] = currentUser
            stockDic['count'] = dataDic['stock_count']
            stockDic['sold'] = '0'
            print("CURRENT USER:", currentUser)
            Stocks.save(stockDic)
            registered = True
        else:
            print(flower_form.errors)
    else:
        flower_form = flowerForm()
    return render(request,'registerProduct.html',
                          {'flower_form':flower_form,
                           'registered':registered})

def easteregg(request):
    registered = False
    if request.method == 'POST':
        gizli_form = gizliForm(data=request.POST)
        if gizli_form.is_valid():
            dataDic = gizli_form.cleaned_data
            print(dataDic)
            Category.save(dataDic)
            registered = True
        else:
            print(gizli_form.errors)
    else:
        gizli_form = gizliForm()
    return render(request,'easteregg.html',
                          {'gizli_form':gizli_form,
                           'registered':registered})

def deleteProduct(request):
    registered = False
    if request.method == 'POST':
        del_form = deletionForm(data=request.POST)
        if del_form.is_valid():
            dataDic = del_form.cleaned_data
            print(dataDic)
            tmp = cursor.execute('Select flower_id From theApp_flower WHERE flower_type = %s', [dataDic['name']]).fetchall()[0][0]
            Flower.delete(dataDic['name'],tmp)
            registered = True
        else:
            print(del_form.errors)
    else:
        del_form = deletionForm()
    return render(request,'deletion.html',
                          {'del_form':del_form,
                           'registered':registered})

def changeProduct(request):
    registered = False
    if request.method == 'POST':
        price_form = updatePriceForm(data=request.POST)
        if price_form.is_valid():
            dataDic = price_form.cleaned_data
            print(dataDic)
            Flower.changePrice(dataDic['flower_type'],dataDic['price'])
            registered = True
        else:
            print(price_form.errors)
    else:
        price_form = updatePriceForm()
    return render(request,'changeProduct.html',
                          {'price_form':price_form,
                           'registered':registered})


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
    
    profile_name = cursor.execute('SELECT username, id FROM theApp_myuser WHERE id = %s', [currentUser]).fetchall()[0][0]
    most_sold = Stocks.objects.raw('SELECT * From theApp_stocks ORDER BY sold DESC LIMIT 5')
    print(most_sold)
    #SELECT * FROM table1 WHERE id IN (SELECT MAX(num1+num2) FROM table2) ORDER BY id DESC limit 5
    flowers = Flower.objects.raw('SELECT * From theApp_flower ORDER BY price DESC LIMIT 4')
    # make magic
    # print(request.user.username) 
    #random_flowers = random.sample(flowers, 5)
    categories =  Category.objects.raw('SELECT * From theApp_category')
    print(categories)
    context = {"profile_name": profile_name, "most_sold": most_sold, "flowers": flowers, "categories": categories} # todo
    return render(request, 'index.html', context)

def seller(request, pk):
    products = cursor.execute('SELECT flower_id_id FROM theApp_products WHERE seller_id_id = %s AND count > 0', [pk]).fetchall()
    seller = pk #?
    categories = cursor.execute('SELECT * From theApp_category').fetchall()
    context = {"products": products, "seller": seller, "categories": categories} # todo
    return render(request, 'seller.html', context)

def products(request):
    categories =  Category.objects.raw('SELECT * From theApp_category')
    flowers = Flower.objects.raw('SELECT * From theApp_flower')
    # make magic
    context = {"flowers": flowers, "categories": categories}
    return render(request, 'products.html', context)

def product(request, pk):
    #flower_id = pk.flower_id
    #profile_name = myUser.objects.raw('SELECT username From theApp_myUser WHERE id = %s', currentUser) # from profile user alma bakilacak
    #favorite_flowers = Faw_Flow.objects.raw('SELECT * From theApp_Faw_Flow WHERE id = %s', currentUser) # from profile get favorited
    print(pk)
    flow_id = cursor.execute('Select flower_id From theApp_flower WHERE photo_id = %s', [pk]).fetchall()[0][0]
    flower = cursor.execute('SELECT photo_id,  description, flower_type, flower_id, occasion, price From theApp_flower WHERE photo_id = %s', [pk]).fetchall() # specific flower with pk
    ph_id = flower[0][0]
    desc = flower[0][1]
    fType = flower[0][2]
    occ = flower[0][4]
    price = flower[0][5]
    stock = cursor.execute('SELECT count, id FROM theApp_stocks WHERE flower_id_id = %s', [flow_id]).fetchall()[0][0] # get flower stock
    
    context = {"flower": flower , "stock": stock, "ph_id": ph_id, "desc": desc, "fType": fType, "occ": occ, "price": price} # todo

    return render(request, 'product.html', context)

def profile(request):
    global currentUser
    userInfo = myUser.objects.raw('SELECT * FROM theApp_myuser WHERE id = %s', currentUser) # get profile
    #userInfoTup = cursor.fetchall()[0]
    orders = Order.objects.raw("SELECT id, price, note, date FROM theApp_order WHERE customer_id = %s", currentUser) # get orders
    #ordersTup = cursor.fetchall()
    favorites = Flower.objects.raw("SELECT F.flower_type FROM myApp_flower F WHERE F.flower_id IN (SELECT F.flower_id FROM myApp_faw_flow WHERE id = %s)", currentUser) # get favorite flowers from fav
    #favTup = cursor.fetchall()
    complaints = Complaint_Report.objects.raw("SELECT order_id_id, status, subject FROM myApp_complaint_report WHERE cust_id_id = %s", currentUser) # get all complaints with user id
    #complaintTup =  cursor.fetchall()
    context = {"temp": temp}
    return render(request, 'profile.html', context)

def about(request):
    return render(request, 'about.html')

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
    forumTopics = Forum_Topic.objects.raw('SELECT * FROM theApp_forum_Topic') # get from forum topics table
    #forumCategories = "todo" # get categories from forum categories
    context = {"forumTopic": forumTopics}
    return render(request, 'forum.html', context)

def postEntry(request, pk):
    postEntry = Forum_Entry.objects.raw('SELECT * FROM theApp_forum_Entry WHERE topic_id = %s' , pk)
    context = {'postEntry': postEntry}
    return render(request, 'postEntry.html',context)

def forumTopic(request, pk):
    forumTopics = Forum_Topic.objects.raw('SELECT * FROM theApp_forum_Topic WHERE topic_id = %s' , pk) # get from forum topics table
    entries = postEntry = Forum_Entry.objects.raw('SELECT * FROM theApp_forum_Entry WHERE topic_id = %s' , pk)
    context = {'forumTopic': formTopic, 'entries': entries}
    return render(request, 'forumTopic.html', context)

def createTopic(request):
    forumCategories = "todo"
    context = {'forumCategories': forumCategories}
    return render(request, 'createTopic.html', context)


def myOrders(request):
    orders = "todo" # Get orders from order delivery
    flower = "todo" # get all flowers
    # then select from orders
    # do this 
    context = {"temp": temp}
    return render(request, 'myOrders.html', context)

def customerService(request):
    reports = Complaint_Report.objects.raw('SELECT order_id_id, subject, status, cust_id_id FROM Complaint_Report') # get cancer from complaint Report
    username = myUser.objects.raw('SELECT Username FROM theApp_myuser WHERE id IN (SELECT cust_id FROM Complaint_Report') # get username with user id from cancer
    context = {"temp": temp}
    return render(request, 'customerService.html', context)

def customerReport(request, pk):
    #using pk get info
    
    return render(request, 'customerReport.html', context)


# Create your views here.
