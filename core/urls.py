from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_query/<selected_dork>', views.get_query, name='get_query'),
    path('search/<dork>', views.search, name='search'),
    path('search-music/', views.search_music, name='search-music'),
]