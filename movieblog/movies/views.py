# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from movies.forms import MovieForm
from reviews.forms import ReviewForm
from .models import Movie, Category


def index(request):
    latest_movies = Movie.objects.all().order_by('-release_date')[:10]
    context = {
        'categories': Category.objects.all(),
        'latest_movies': latest_movies,
    }
    return render(request, 'index.html', context)


def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    error = ''
    recommendations = Movie.objects.filter(
        category=movie.category).exclude(pk=movie_pk)

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

    avg_rating = Movie.avg_rating(movie)

    if request.user.is_staff:
        reviews = movie.reviews.a_moderar()
    else:
        reviews = movie.reviews.aceptado()

    context = {'movie': movie, 'review_form': review_form,
               'error': error, 'avg_rating': avg_rating, 'recommendations': recommendations, 'reviews': reviews}
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


def movie_list(request):
    category = request.GET.get('category')
    movies = Movie.objects.all()
    if category:
        movies = movies.filter(category__pk=category)
    categories = Category.objects.all()
    paginator = Paginator(movies, 2)
    page = request.GET.get('page')
    try:
        movie_page = paginator.page(page)
    except PageNotAnInteger:
        movie_page = paginator.page(1)
    except EmptyPage:
        movie_page = paginator.page(paginator.num_pages)
    context = {
        'movies': movies,
        'categories': categories,
        'movie_page': movie_page,
    }
    return render(request, 'movie_list.html', context)
