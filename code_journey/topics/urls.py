from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('', views.home, name='home'),
]

def home(request):
    return HttpResponse("Welcome to my LeetCode journey!")