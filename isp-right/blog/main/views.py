from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'title': 'Main window'})

def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})