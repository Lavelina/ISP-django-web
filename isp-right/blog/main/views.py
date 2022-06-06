from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, Http404
from django.shortcuts import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import *
from .models import *
from .utils import *


class Home(DataMixin, ListView):

    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Post.objects.filter(status=True)


def about(request):
    return render(request, 'main/about.html', {'title': 'About us'})


class Add(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpost.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=" Добавление поста")
        return dict(list(context.items()) + list(c_def.items()))



class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowSection(DataMixin, ListView):
    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(sect__slug=self.kwargs['sect_slug'], status=True)

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].sect),
                                          sect_selected=context['posts'][0].sect_id)
            return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Регистрация")
            return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data(**kwargs)
            c_def = self.get_user_context(title="Вход")
            return dict(list(context.items()) + list(c_def.items()))


def user_logout(request):
    logout(request)
    return redirect('login')