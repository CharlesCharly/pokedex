from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('api/pokedex/', views.PokemonList.as_view(), name='pokemon-list'),
    path('api/pokemon/<int:pokedex_number>/', views.PokemonDetail.as_view(), name='pokemon-detail'),
    path('api/pokemon_types/', views.get_all_pokemon_types, name='pokemon-types')
]
