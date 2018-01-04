# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Review


def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    error = ''
    if request.method == 'POST':
        if request.user.is_staff:
            state = request.POST.get('state', None)
            if state == 'ok':
                review.state = state
            elif state == 'notok':
                review.state = state
            review.save()
            return redirect(reverse('reviews:detail', args=(review.pk, )))
        else:
            error = 'El usuario debe ser staff para modificar el estado de una review'
    context = {
        'review': review,
        'error': error,
    }
    return render(request, 'review_detail.html', context)

# Create your views here.
