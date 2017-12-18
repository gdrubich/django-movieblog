# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from reviews.forms import ReviewForm
from .models import Movie, Category


def index(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    error = ''

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)

        if request.user.is_authenticated():
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.movie = movie
                new_review.user = request.user
                new_review.save()

                return redirect(reverse('movies:detail', args=(movie.pk, )))
        else:
            error = 'Debes estar logeado para dejar una review'

    review_form = ReviewForm()
    context = {'movie': movie, 'review_form': review_form, 'error': error}
    return render(request, 'movie_detail.html', context)
