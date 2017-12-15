# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


#class ReviewsInfo(models.Model):
#	average_rating = 


class Review(models.Model):
	user = models.ForeignKey(User)
	movie = models.ForeignKey('movies.Movie')
	#rating = models.
	description = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def add_review(self, movie_id):
		pass