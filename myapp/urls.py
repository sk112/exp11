from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', home_page.homepage, name ='home'),
    path('content/', home_page.content , name='content'),
    path('create/', view1.question_create_form, name = 'QCreateForm'),
    path('answer/<int:pk>',view1.answer_create_form, name = 'ACreateForm'),
]
