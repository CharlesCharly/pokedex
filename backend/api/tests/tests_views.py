from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Pokemon
from .tests_factories import create_test_pokemon

class PokemonListTests(TestCase):
  def setUp(self):
    self.client = APIClient()

  def test_list_pokemons(self):
    url = reverse('pokemon-list')
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class PokemonDetailTests(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.pokemon = create_test_pokemon()

  def test_retrieve_pokemon(self):
    url = reverse('pokemon-detail', kwargs={'nb': self.pokemon.pokedex_number})
    response = self.client.get(url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
