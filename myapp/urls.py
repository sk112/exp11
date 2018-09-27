from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('v1', view1.index, name ='v1'),
]