
from django import forms

class create_question_form(forms.Form):
    Question = forms.CharField(widget=forms.Textarea,label='Question',max_length=200)
    by = forms.CharField(label='by', max_length=50)

class create_answer_form(forms.Form):
    Answer = forms.CharField(widget=forms.Textarea,label = 'answer', max_length=400)
    by = forms.CharField(label = 'by', max_length=50)

