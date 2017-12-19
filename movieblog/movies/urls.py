from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movies/(?P<movie_pk>\d+)/$', views.movie_detail, name='detail'),
    url(r'^movies/add$', views.movie_add, name='add')
]
