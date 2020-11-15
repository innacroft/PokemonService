from pokemon.models import Pokemon,Evolution
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PokemonSerializer
from rest_framework import generics


class PokemonDetails(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = PokemonSerializer
    name='pokemon_details'
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        name = self.kwargs['name']
        objects=Evolution.objects.filter(id_chain=18).values_list('pokemon_id','evolves_to')
        
        return Pokemon.objects.filter(name=name)

