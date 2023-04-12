from rest_framework import serializers
from moviesapi.models import Movies, MoviesDetails


class MoviesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"

owner=serializers.ReadOnlyField(source='owner.username')        

class MoviesDEtailsSerializers(serializers.ModelSerializer):
    class Meta: 
        model=MoviesDetails     
        fields='__all__'