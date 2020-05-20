from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain

def index(request):

    profile_name = "todo" # from profile user alma bakilacak
    most_sold = "todo" # from stocks
    flowers = "todo" # butun flowerlar Select * From Flowers
    # make magic
    random_flowers = "todo"
    categories = "todo" # get all categories
    context = ["profile_name": profile_name, "most_sold": most_sold] # todo
    return render(request, 'index.html', context)

def seller(request, pk):
    profile_name = "todo" # from profile user alma bakilacak
    products = "todo" # get products from stocks
    seller = "todo" # get seller with pk
    categories = "todo" # get all categories
    context = ["products": products, "seller": seller] # todo
    return render(request, 'seller.html', context)

def product(request, pk):
    profile_name = "todo" # from profile user alma bakilacak
    favorite_flowers = "todo" # from profile get favorited
    flower = "todo" # specific flower with pk
    stock = "todo" # get flower stock
    context = ["flower": flower] # todo
    return render(request, 'product.html', context)

def profile(request):
    profile = "todo" # get profile
    orders = "todo" # get orders
    favorites = "todo" # get favorite flowers from fav
    complaint = "todo" # get all complaints with user id
    context = "todo"
    return render(request, 'profile.html', context)

def contact(request):
    return render(request, 'contact.html')

def contact(request):
    return render(request, 'aboutus.html')

def order(request, pks):
    # pks is a list
    stocks = "todo" # get stocks of flowers
    chocolate = "todo" # get chocolate
    context = "todo"
    return render(request, 'order.html')

def loginSign(request):
    return render(request, 'login.html')

def changePassword(requst):
    return render(request, 'changePass.html')

def forum(request):
    forumTopics = "todo" # get from forum topics table
    forumCategories = "todo" # get categories from forum categories
    context = "todo"
    return render(request, 'forum.html')

def postEntry(request, pk):
    forumTopic = "todo" 
    context = ['forumTopic' = formTopic]
    return render(request, 'postEntry.html',context)

def forumTopic(request, pk):
    forumTopic = "todo" # get topic with pk
    entries = "todo" #from forumEntry table
    context = ['forumTopic' = formTopic]
    return render(request, 'forumTopic.html', context)

def createTopic(request):
    forumCategories = "todo"
    context = ['forumCategories' = forumCategories]
    return render(request, 'createTopic.html', context)

def addFlover(request):
    return render(request, 'addFlower.html', context)

def myOrders(request):
    orders = "todo" # Get orders from order delivery
    flower = "todo" # get all flowers
    # then select from orders
    # do this 
    return render(request, 'myOrders.html', context)

def customerService(request):
    cancer = "todo" # get cancer from complaint Report
    username = "todo" # get username with user id from cancer
    return render(request, 'customerService.html', context)

def customerReport(request, pk):
    #using pk get info
    return render(request, 'customerReport.html', context)


# Create your views here.
