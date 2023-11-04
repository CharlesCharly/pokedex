from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .tests_factories import create_test_pokemon

class PokemonListTests(TestCase):
  def setUp(self):
    self.client = APIClient()

  def test_list_pokemons(self):
    # Set the custom header indicating a front-end request
    headers = {'HTTP_X_FRONTEND_REQUEST': 'true'}

    # Define query parameters matching the view's parameters
    query_params = {
        'searchQuery': 'charm',
        'sortFilter': 'pokedex_number',
        'typeFilter': 'all_types',
        'asc': 'true',
    }

    url = reverse('pokemon-list')
    response = self.client.get(url, query_params, **headers)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_list_pokemons_no_search_query(self):
    # Set the custom header indicating a front-end request
    headers = {'HTTP_X_FRONTEND_REQUEST': 'true'}

    # Test listing all Pokemons without a search query
    query_params = {
      'searchQuery': '',
      'sortFilter': 'pokedex_number',
      'typeFilter': 'all_types',
      'asc': 'true',
      'page': 1,
    }

    url = reverse('pokemon-list')
    response = self.client.get(url, query_params, **headers)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_list_pokemons_pagination(self):
    # Set the custom header indicating a front-end request
    headers = {'HTTP_X_FRONTEND_REQUEST': 'true'}

    # Test listing Pokemons with pagination
    query_params = {
        'searchQuery': 'charm',
        'sortFilter': 'pokedex_number',
        'typeFilter': 'all_types',
        'asc': 'true',
        'page': 1,
    }
    url = reverse('pokemon-list')
    response = self.client.get(url, query_params, **headers)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


class PokemonDetailTests(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.pokemon = create_test_pokemon()

  def test_retrieve_pokemon(self):
    # Set the custom header indicating a front-end request
    headers = {'HTTP_X_FRONTEND_REQUEST': 'true'}

    # Test attempting to retrieve existing Pokemon
    url = reverse('pokemon-detail', kwargs={'pokedex_number': self.pokemon.pokedex_number})
    response = self.client.get(url, **headers)
    self.assertEqual(response.status_code, status.HTTP_200_OK)


  def test_retrieve_nonexistent_pokemon(self):
    # Set the custom header indicating a front-end request
    headers = {'HTTP_X_FRONTEND_REQUEST': 'true'}

    # Test attempting to retrieve a Pokemon that doesn't exist
    url = reverse('pokemon-detail', kwargs={'pokedex_number': 9999})
    response = self.client.get(url, **headers)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
