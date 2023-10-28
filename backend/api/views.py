from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonList(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
