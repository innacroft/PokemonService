from pokemon.models import Pokemon,Evolution
from rest_framework import serializers


class PokemonSerializer(serializers.ModelSerializer):
    foo = serializers.ReadOnlyField()

    class Meta:
        model = Pokemon
        fields ='__all__'
        


        