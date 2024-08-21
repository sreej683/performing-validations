from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse


def insert_webpage(request):
    EWO=WebPageForm()
    d={'EWO':EWO}
    if request.method=='POST':
        WFDO=WebPageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']
            TO=Topic.objects.get(topic_name=tn)
            WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
            WO.save()
            return HttpResponse('Webpage is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,'insert_webpage.html',d)