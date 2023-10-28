from rest_framework import serializers
from .models import Pokemon

# JSON data <> Python data structures
class PokemonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['name', 'type1', 'type2', 'pokedex_number', 'height_m', 'weight_kg']

# JSON data <> Python data structures
class PokemonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
