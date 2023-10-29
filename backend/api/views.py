from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonListSerializer, PokemonDetailSerializer
from django.http import Http404

class PokemonList(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonListSerializer


class PokemonDetail(generics.RetrieveAPIView):
    serializer_class = PokemonDetailSerializer

    def get_object(self):
        nb = self.kwargs.get('nb')

        try:
            return Pokemon.objects.get(pokedex_number=nb)
        except Pokemon.DoesNotExist:
            raise Http404("Pokemon not found")
