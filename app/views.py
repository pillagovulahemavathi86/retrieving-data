from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db import Q

def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)

    


def display_webpages(request):
    QSW=Webpages.objects.all()
    QSW=Webpages.objects.all().filter(topic_name='cricket')
    QSW=Webpages.objects.all().exclude(topic_name='cricket')
    QSW=Webpages.objects.all()[:5:]
    QSW=Webpages.objects.all().order_by('topic_name')
    QSW=Webpages.objects.all().order_by('-topic_name')
    QSW=Webpages.objects.all().order_by(Length('name'))
    #QSW=Webpages.objects.all().order_by(Length('name')).desc()
    QSW=Webpages.objects.all().filter(url__startswith='http')
    QSW=Webpages.objects.all().filter(name__startswith='d')
    QSW=Webpages.objects.all().filter(name__contains='a')
    QSW=Webpages.objects.all().filter(name__regex='\w{7}')
    QSW=Webpages.objects.all().filter(name__in=['dhoni','arun'])
    QSW=Webpages.objects.all().filter(Q(topic_name='cricket')&Q(name='arun'))


    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
    


def accessrecords(request):
    QWA=AccessRecords.objects.all()
    d={'accessrecords':QWA}
    return render(request,'accessrecords.html',d)
