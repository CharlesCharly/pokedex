from django.http import JsonResponse
from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonListSerializer, PokemonDetailSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django.http import Http404
from django.db.models import Q

class PokemonList(generics.ListAPIView):
    serializer_class = PokemonListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['pokedex_number', 'height_m', 'weight_kg']
    search_fields = ['name, type1', 'type2']

    # Define a base queryset
    queryset = Pokemon.objects.all()

    def get_queryset(self):
        # Start with the base queryset
        queryset = self.queryset

        search_query = self.request.query_params.get('searchQuery')
        sort_filter = self.request.query_params.get('sortFilter')
        type_filter = self.request.query_params.get('typeFilter')
        asc = self.request.query_params.get('asc')
        second_filter_field = 'pokedex_number'

        # Create an initial Q object
        filters = Q()

        # Apply if the user has typed 2 or more characters
        if search_query is not None and len(search_query) >= 2:
            filters &= Q(name__icontains=search_query)

        # Ignore if the filter is on "all"
        if type_filter != "all":
            filters &= Q(Q(type1=type_filter) | Q(type2=type_filter))

        # Apply sorting
        if asc == 'true':
            queryset = queryset.filter(filters).order_by(sort_filter, second_filter_field)
        else:
            queryset = queryset.filter(filters).order_by(f'-{sort_filter}', f'-{second_filter_field}')

        return queryset


class PokemonDetail(generics.RetrieveAPIView):
    serializer_class = PokemonDetailSerializer
    queryset = Pokemon.objects.all()
    lookup_field = 'pokedex_number'

    def get_object(self):
        pokedex_number = self.kwargs.get(self.lookup_field)
        try:
            return self.queryset.get(pokedex_number=pokedex_number)
        except Pokemon.DoesNotExist:
            raise Http404("Pokemon not found")


def get_all_pokemon_types(request):
    # Get non Null flat list of values
    type1 = Pokemon.objects.exclude(type1='').values_list('type1', flat=True)
    type2 = Pokemon.objects.exclude(type2='').values_list('type2', flat=True)

    # Create a list with distinct values from the 2 types
    distinct_types = list(set(type1) | set(type2))

    # Filter out Null values and sort the list
    filtered_distinct_types = [type for type in distinct_types if type is not None]

    types_list = sorted(filtered_distinct_types)

    # Response is an array and not a JSON object w/ safe=False
    return JsonResponse(types_list, safe=False)
