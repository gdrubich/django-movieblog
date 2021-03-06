"""movieblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from movies import views as movieviews
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('movies.urls', namespace='movies')),
    url(r'^ratings/', include('star_ratings.urls',
                              namespace='ratings', app_name='ratings')),
    url(r'bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^movies/', movieviews.movie_list, name='movies_list'),
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^search/', include('haystack.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
