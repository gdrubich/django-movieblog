# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import Movie


class MovieForm(ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'category',
                  'description', 'release_date', 'country', 'director', 'actor', ]
