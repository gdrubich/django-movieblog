# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from movies.forms import MovieForm
from reviews.forms import ReviewForm
from .models import Movie, Category


def index(request):
    context = {
        'movies': Movie.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html')


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


@login_required()
@user_passes_test(lambda u: u.is_staff, login_url='/login/')
def movie_add(request):
    error = ''
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)
        if movie_form.is_valid():
            # Si el form es valido guardar la data en una variable sin pegarle a la
            # base de datos, para agregar info que esta en el request
            new_movie = movie_form.save(commit=False)
            # Agregar user desde request
            new_movie.user = request.user
            # Guardar en base de datos
            new_movie.save()
            return redirect(reverse('movies:index'))
        else:
            error = 'El formulario no es valido'
    else:
        movie_form = MovieForm()
    context = {'movie_form': movie_form, 'error': error}
    return render(request, 'movie_add.html', context)

