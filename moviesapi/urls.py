from django.contrib import admin
from django.urls import path, include
from moviesapi.views import MoviesViewset, MoviesDetailsViewset
from rest_framework import routers

routers=routers.DefaultRouter()
routers.register(r'movieslist', MoviesViewset)
routers.register(r'details', MoviesDetailsViewset)


urlpatterns = [
    path('', include(routers.urls))
]