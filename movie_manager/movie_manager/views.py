from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def viewAllMovies(request): 
    movies = Movie.objects.all()
    movies_sr = MovieSerializer(movies, many=True)
    return Response({'status': 200, 'movies': movies_sr.data})

@api_view(['POST'])
def create_movie(request): 
    movie_sr = MovieSerializer(data=request.data)

    if not movie_sr.is_valid(): 
        return Response({'status': 403, 'message': 'Serializer is not valid'})
    
    movie_sr.save()
    return Response({'status': 200, 'movie': movie_sr.data})

@api_view(['PATCH'])
def edit_movie(request, id): 
    try: 
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist(): 
        return Response({'status': 403, 'message': "Movie does not exist"})
    
    movie_sr = MovieSerializer(movie, data=request.data)
    if not movie_sr.is_valid(): 
        return Response({'status': 403, 'message': 'Serializer is not valid'})
    
    movie_sr.save()
    return Response({'status': 200, 'movie': movie_sr.data})

@api_view(['DELETE'])
def delete_movie(request, id): 
    try: 
        movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist(): 
        return Response({'status': 403, 'message': "Movie does not exist"})
    
    movie.delete()
    return Response({'status': 200, 'message': "Movie deleted successfully"})
