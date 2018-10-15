from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.models import *
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import *
from .form_views import *
from . import home_page


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
         'latest_question_list': latest_question_list,
    }
    return render(request,'index.html',context)
    #return HttpResponse(template.render(context, request))


def indexPerID(request,question_id):
    return HttpResponse("Hello: question is: %d" % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def question_create_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = create_question_form(request.POST)
        # check whether it's valid:
        if form.is_valid():

            title = form.cleaned_data['Title']
            desc = form.cleaned_data['Description']
            by = form.cleaned_data['by']

            q = Question(question_text=desc, question_title=title, question_by=by)
            q.save()

            # redirect to a new URL:
            return redirect(to='content', permanent=True)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = create_question_form()

    return render(request,'QCreateForm.html',{'form': form})


def answer_create_form(request,pk):

    if request.method == 'POST':
        form = create_answer_form(request.POST)

        if form.is_valid():
            ans = request.POST.get('Answer')
            by = request.POST.get('by')
            ans = Question.objects.get(id=pk)
            a = Answer(answered_by=by, answer_text=ans, pub_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), answers=ans)
            a.save()

            return redirect(to='content', permanent=True)
    else:
        form = create_answer_form()
    return render(request,'ACreateForm.html', {'form': form , 'pk':pk})