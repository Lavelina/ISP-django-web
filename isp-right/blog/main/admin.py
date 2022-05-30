from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Section, SectionAdmin)