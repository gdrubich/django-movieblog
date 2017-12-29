# -*- coding: utf-8 -*-
import datetime
from haystack import indexes
from movies.models import Movie, Director


class MovieIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    director = indexes.CharField(model_attr='director')
    release_date = indexes.DateTimeField(model_attr='release_date')

    def get_model(self):
        return Movie

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(release_date__lte=datetime.datetime.now())
