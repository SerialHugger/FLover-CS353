from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain

def index(request):
    return render(request, 'index.html')
# Create your views here.
