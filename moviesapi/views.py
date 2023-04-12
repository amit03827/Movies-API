from django.shortcuts import render
from rest_framework import viewsets
from moviesapi.models import Movies, MoviesDetails
from moviesapi.serializers import MoviesSerializers, MoviesDEtailsSerializers
from rest_framework.response import Response
from rest_framework.decorators import action 
from rest_framework .authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from moviesapi.permissions import IsreadOnly




class MoviesViewset(viewsets.ModelViewSet):
    queryset=Movies.objects.all()
    serializer_class=MoviesSerializers

    permission_classes=[permissions.IsAuthenticatedOrReadOnly, IsreadOnly]

    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)

    

    # movies/{moviesID}/moviesdetails

    @action(detail=True, methods=['get'])
    def moviesdetails(self, request, pk=None):
        movies=Movies.objects.get(pk=pk)
        moviesData=MoviesDetails.objects.filter(movies=movies)
        movies_serializers=MoviesDEtailsSerializers(moviesData, many=True, context={'request':request})
        return Response(movies_serializers.data)
        
        

class MoviesDetailsViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=MoviesDetails.objects.all()
    serializer_class=MoviesDEtailsSerializers    
