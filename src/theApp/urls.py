from django.urls import path
from django.views import defaults
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'theApp'

urlpatterns = [
    path("", views.user_login, name='user_login'),
    path("user_logout", views.user_logout, name='user_logout'),
    path("user_login", views.user_login, name='user_login'),
    path("registration", views.register, name='register'),
    path("index", views.index, name='index'),
    path("registerProduct", views.registerProduct, name='registerProduct'),
    path("changeProduct", views.changeProduct, name='changeProduct'),
    path("easteregg", views.easteregg, name='easteregg'),
    path("deletion", views.deleteProduct, name='deleteProduct'),
    path("products", views.products, name='products'),
    path("about", views.about, name='about'),
    path("<int:pk>", views.product, name='product'),
    #path("contact", views.contact, name='contact'),
    #path("blog", views.blog, name='blog'),

     # debug
    path("404", defaults.page_not_found, ),
]

urlpatterns += staticfiles_urlpatterns()