from django.urls import path
from django.views import defaults
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    #path("contact", views.contact, name='contact'),
    #path("blog", views.blog, name='blog'),

     # debug
    path("404", defaults.page_not_found, ),
]

urlpatterns += staticfiles_urlpatterns()