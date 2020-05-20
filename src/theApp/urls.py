from django.urls import path
from django.views import defaults
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'theApp'

urlpatterns = [
    path("", views.user_login, name='user_login'),
    path("user_login", views.user_login, name='user_login'),
    path("registration", views.register, name='register'),
    path("index", views.index, name='index'),
    #path("contact", views.contact, name='contact'),
    #path("blog", views.blog, name='blog'),

     # debug
    path("404", defaults.page_not_found, ),
]

urlpatterns += staticfiles_urlpatterns()