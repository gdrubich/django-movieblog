from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^review/(?P<review_pk>\d+)/$', views.review_detail, name='detail'),
]
