from django.test import TestCase
from api.serializers import PokemonListSerializer, PokemonDetailSerializer
from .tests_factories import create_test_pokemon

class PokemonSerializerTests(TestCase):
  def setUp(self):
    self.pokemon = create_test_pokemon()

  def test_pokemon_list_serializer(self):
    serializer = PokemonListSerializer(instance=self.pokemon)
    expected_fields = ['name', 'type1', 'type2', 'pokedex_number', 'height_m', 'weight_kg']
    for field in expected_fields:
      self.assertIn(field, serializer.data)

  def test_pokemon_detail_serializer(self):
    serializer = PokemonDetailSerializer(instance=self.pokemon)
    self.assertEqual(serializer.data['name'], self.pokemon.name)
    self.assertEqual(serializer.data['sp_attack'], self.pokemon.sp_attack)
    self.assertEqual(serializer.data['generation'], self.pokemon.generation)
    # Can add more assertEqual if needed
