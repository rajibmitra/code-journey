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
    topics_tree = {
        'name': 'Arrays',
        'left': {'name': 'Two Pointers'},
        'right': {'name': 'Stack'}
    }
    return render(request, 'home.html', {'topics_tree': topics_tree})

