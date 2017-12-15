# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# A function that returns the path to a movie according to its Id
# Not working yet


def cover_upload_path(instance, filename):
    return '/'.join(['cover', str(instance.id), filename])


class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('movies.Category')
    description = models.TextField()
    release_date = models.DateField(default=timezone.now)
    director = models.ForeignKey('movies.Director')
    actor = models.ManyToManyField('movies.Actor')
    #country = CountryField()
    cover_img = models.ImageField(
        upload_to=cover_upload_path, default='/covers/default_cover.jpeg')


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    #country = CountryField()

    class Meta:
        abstract = True


class Director(Person):
    pass


class Actor(Person):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    referents = models.ForeignKey(Movie)



