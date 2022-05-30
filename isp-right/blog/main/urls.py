from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', add, name='add_page'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('section/<int:sect_id>/', show_section, name='section'),
]

