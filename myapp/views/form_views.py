
from django import forms
from tinymce import widgets
from tinymce.widgets import TinyMCE


class create_question_form(forms.Form):
    Title = forms.CharField(widget=forms.TextInput, label='Title', max_length=200)
    Description = forms.CharField(widget=forms.Textarea,label='Question',max_length=1024)
    by = forms.CharField(label='by', max_length=50)


class create_answer_form(forms.Form):
    Answer = forms.CharField(widget = forms.Textarea,label = 'answer', max_length=400)
    by = forms.CharField(label = 'by', max_length=50)
