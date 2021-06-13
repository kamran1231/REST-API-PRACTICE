# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse
#
# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(data)
#
#
# def movie_details(request,id):
#     movies = Movie.objects.get(id=id)
#     data = {
#         'name':movies.name,
#         'description':movies.description,
#         'active':movies.active
#     }
#
#     return JsonResponse(data)
