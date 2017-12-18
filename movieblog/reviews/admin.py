# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Review

class ReviewAdmin (admin.ModelAdmin):
    list_display = ('user', 'rating', 'movie')

admin.site.register(Review, ReviewAdmin)
