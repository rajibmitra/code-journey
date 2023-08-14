from django.shortcuts import render
from .models import Topic
from django.http import HttpResponse

def index(request):
    root_topic = Topic.objects.get(name="Arrays")
    return render(request, 'topics/index.html', {'root_topic': root_topic})

def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'topics/topic_detail.html', {'topic': topic})

def home(request):
    return HttpResponse("Welcome to my LeetCode journey!")
