# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Review(models.Model):

    STAR_RATINGS = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star')
    )

    user = models.ForeignKey(User)
    movie = models.ForeignKey('movies.Movie', related_name='reviews')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=STAR_RATINGS)
