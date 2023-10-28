from rest_framework import serializers
from .models import Pokemon

# JSON data <> Python data structures
class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
