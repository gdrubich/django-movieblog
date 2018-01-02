# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class ReviewQuerySet(models.QuerySet):
    def a_moderar(self):
        return self.filter(state='mod')

    def aceptado(self):
        return self.filter(state='ok')

    def rechazado(self):
        return self.filter(state='notok')


class Review(models.Model):

    STAR_RATINGS = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star')
    )

    STATES = (
        ('mod', 'Moderar'),
        ('ok', 'Aceptado'),
        ('notok', 'Rechazado'),
    )

    user = models.ForeignKey(User)
    movie = models.ForeignKey('movies.Movie', related_name='reviews')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=STAR_RATINGS)
    state = models.CharField(choices=STATES, default='mod', max_length=100)
    states = ReviewQuerySet.as_manager()
