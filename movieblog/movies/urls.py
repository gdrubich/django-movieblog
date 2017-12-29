from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/(?P<movie_pk>\d+)/$', views.movie_detail, name='detail'),
    url(r'^movies/add$', views.movie_add, name='add'),
    url(r'^search/', views.search, name='search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
