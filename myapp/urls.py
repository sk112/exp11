from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('homepage/', home_page.homepage , name='home_page'),
]
