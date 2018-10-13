from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.models import *
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404

def homepage(request):
    q_list = Question.objects.all()

    a_list = {}
    a_list_size = {}
    for i in q_list:
        a_list[i.id]  = Answer.objects.filter(answers = i.id)
        a_list_size[i.id] = len(a_list[i.id])

    context = {
        'q_list' : q_list,
        'a_list' : a_list,
        'a_list_size' : a_list_size,
    }
    return render(request, 'homepage.html', context)