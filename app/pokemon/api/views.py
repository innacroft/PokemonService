from rest_framework.views import APIView
from django.http import JsonResponse
from pokemon.models import Pokemon, Evolution
class PokemonDetails(APIView):
    """
    API endpoint to show Pokemon details from name
    """
    def get(self, request, name, format=None, **kwargs):
        try:
            obj=Pokemon.objects.filter(name=name).values()
            if obj:
                id_pokemon=obj[0].get('pokemon')
                evlist=Evolution.objects.filter(pokemon=id_pokemon).values()
                return JsonResponse({
                    'pokemon_info': list(obj),
                    'evolution': list(evlist),
                })
            else:
                return JsonResponse({
                'Error': 'Pokemon doesnt exist!',
            })
        except Exception as e: 
            return JsonResponse({
                'Error': e,
            })

