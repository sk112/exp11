from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('home/', home_page.homepage , name='home'),
    path('home/create/', view1.get_name, name = 'createForm'),
]
