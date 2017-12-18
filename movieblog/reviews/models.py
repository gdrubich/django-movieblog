# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie


class Review(models.Model):
    user = models.ForeignKey(User)
    movie = models.ForeignKey('movies.Movie')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    STAR_RATINGS = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'))
    rating = models.IntegerField(choices=STAR_RATINGS)

    def add_review(self, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        new_review = Review.objects.create(
            user=self.user,
            movie=movie,
            title=self.title,
            description=self.description,
            date=self.date,
            rating=self.rating)
        new_review.save()

    def edit_review(self):

        pass

    def delete_review(self, movie_id):
        pass
