from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', viewAllMovies),
    path('movies/create/', create_movie),
    path('movies/edit/<int:id>/', edit_movie),
    path('movies/delete/<int:id>/', delete_movie)
]
