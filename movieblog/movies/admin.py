# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Actor, Movie, Category, Director

class MovieAdmin (admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director')
    filter_horizontal = ('actor',)

class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'description')

class DirectorAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class ActorAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
