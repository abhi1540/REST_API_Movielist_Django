from django.conf.urls import url
from moviesapp import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^movies/$', views.movie_list),
    url(r'^movies/(?P<pk>[0-9]+)/$', views.movie_detail),
]
