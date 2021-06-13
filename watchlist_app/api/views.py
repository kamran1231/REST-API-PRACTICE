
from rest_framework.views import APIView
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status

class MovieList(APIView):
    def get(self,request,format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class MovieDetail(APIView):
    def get(self,request,id):
        try:
            movies = Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)


    def put(self,request,id):
        movies = Movie.objects.get(id=id)
        serializer = MovieSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self,request,id):
        movies = Movie.objects.get(id=id)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





'''<<<<======================Function Base View=========================>>>'''
# from rest_framework.response import Response
# from watchlist_app.models import Movie
# from .serializers import MovieSerializer
# from rest_framework.decorators import api_view
# from rest_framework import status


# @api_view(['GET', 'POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
#
#
#
# @api_view(['GET', 'PUT','DELETE'])
# def movie_details(request,id):
#
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)
#
#     if request.method == 'PUT':
#         movies = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(id=id)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)








