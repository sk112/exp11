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
from .home_page import createForm
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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = createForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            question = form.cleaned_data['Question']
            by = form.cleaned_data['by']

            q = Question(question_text = question, question_by = by , pub_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            q.save()

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return redirect(to='home',permanent=True)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = createForm()

    return render(request, 'QCreateForm.html', {'form': form})