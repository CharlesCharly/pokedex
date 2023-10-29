from django.test import TestCase
from api.models import Pokemon
from .tests_factories import create_test_pokemon

class PokemonModelTests(TestCase):
  def test_pokemon_str(self):
    pokemon = Pokemon(name="Test Pokemon", pokedex_number=1)
    self.assertEqual(str(pokemon), "Test Pokemon")

  def test_pokemon_creation(self):
    pokemon = create_test_pokemon()
    self.assertEqual(Pokemon.objects.count(), 1)
