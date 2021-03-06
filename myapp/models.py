from django.db import models

# Create your models here.

from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

class Question(models.Model):
    question_by = models.CharField(max_length=200)
    question_title = models.CharField(max_length=200, default='No Title')
    question_text = RichTextField(max_length=1024)
    pub_date = models.DateTimeField(auto_now_add=True)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_by


class Answer(models.Model):
    answered_by = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    answer_text = models.CharField(max_length=400)
    answers = models.ForeignKey(Question, on_delete=models.CASCADE)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.answered_by

#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
