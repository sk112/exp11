from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('', view1.index, name='index'),
    path('<int:question_id>/', view1.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', view1.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', view1.vote, name='vote'),
]