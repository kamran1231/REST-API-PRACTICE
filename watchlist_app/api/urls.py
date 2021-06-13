

from django.urls import path
from watchlist_app.api.views import MovieList,MovieDetail

urlpatterns = [
    path('', MovieList.as_view(),name='movie_list'),
    path('<int:id>/', MovieDetail.as_view(),name='movie_details'),
]




'''<======Function Urls======>'''
# urlpatterns = [
#     path('', views.movies_list,name='movie_list'),
#     path('<int:id>/', views.movie_details,name='movie_details'),
# ]