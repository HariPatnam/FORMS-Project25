from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=TOPIC.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic_name is inserted ')
    return render(request,'insert_topic.html')



def insert_webpage(request):
    LTO=TOPIC.objects.all()
    d={'topics':LTO}

    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']

        TO=TOPIC.objects.get(topic_name=topic)

        WO=Webpages.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse ('INSERT_WEBPAGE IS INSERTED ')

    return render (request,'insert_webpage.html',d)


