from django.contrib import admin
from moviesapi.models import Movies, MoviesDetails

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display=('name','year','type')

admin.site.register(Movies, MoviesAdmin)

class MoviesAdminD(admin.ModelAdmin):
    list_display=('director_name','collection', 'movies')
admin.site.register(MoviesDetails, MoviesAdminD)
