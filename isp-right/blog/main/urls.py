from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('addpage/', Add.as_view(), name='add_page'),
    path('<slug:post_slug>/delete/', DeletePost.as_view(), name='delete-post'),
    path('<slug:post_slug>/update/', UpdatePost.as_view(), name='update-post'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('section/<slug:sect_slug>/', ShowSection.as_view(), name='section'),
]

