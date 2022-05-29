from django.http import HttpResponse
from django.shortcuts import render

from .models import *

menu = ["About us", "Add", "Feedback", "Sign in"]

def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts, 'menu': menu, 'title': 'Main window'})