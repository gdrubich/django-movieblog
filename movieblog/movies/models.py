a  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.db.models import Avg


# A function that returns a created path to a movie cover


def cover_upload_path(instance, filename):
    return '/'.join(['cover', instance.category.name, filename])


class Movie(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey('movies.Category')
    description = models.TextField(max_length=140)
    release_date = models.DateField(default=timezone.now)
    director = models.ForeignKey('movies.Director')
    actor = models.ManyToManyField('movies.Actor')
    country = CountryField()
    cover_img = models.ImageField(
        upload_to=cover_upload_path, default='/covers/default_cover.jpeg', null=True)

    def __unicode__(self):
        return "%s" % (self.title)

    def avg_rating(self):
        return self.reviews.all().aggregate(Avg('rating')).get('rating__avg', None)

    class Meta:
        ordering = ['-release_date']


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = CountryField()

    def __unicode__(self):
        return "%s, %s" % (self.first_name, self.last_name)

    class Meta:
        abstract = True


class Director(Person):
    pass


class Actor(Person):
    pass


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __unicode__(self):
        return "%s" % (self.name)
