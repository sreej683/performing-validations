from django import forms
from app.models import *



def check(subvalue):
    if subvalue[0].lower()=='a':
        raise forms.ValidationError('value a is presented')

def check_length(subvalue):
    if len(subvalue)>5:
        raise forms.ValidationError('length is lower')


class WebPageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100,validators=[check,check_length])
    url=forms.URLField()
    email=forms.EmailField()





    