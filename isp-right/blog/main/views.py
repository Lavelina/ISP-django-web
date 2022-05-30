from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import *


def index(request):
    posts = Post.objects.all()
    sects = Section.objects.all()

    context = {
        'posts': posts,
        'sects': sects,
        'title': 'Main Window',
        'sect_selected': 0,
    }

    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})

def add(request):
    return render(request, 'main/about.html', {'title': 'Add post'})

def contacts(request):
    return render(request, 'main/about.html', {'title': 'Contacts'})

def login(request):
    return render(request, 'main/about.html', {'title': 'Login'})

def show_post(request, post_id=None):
    return HttpResponse(f"Post with id = {post_id}")

def show_section(request, sect_id):
    posts = Post.objects.filter(sect_id=sect_id)
    sects = Section.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'sects': sects,
        'title': 'Chosen category',
        'sect_selected': sect_id,
    }
    return render(request, 'main/index.html', context=context)