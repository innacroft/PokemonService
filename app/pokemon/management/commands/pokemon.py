from django.core.management.base import BaseCommand
from ...views import Create_pokemon

class Command(BaseCommand):
    help = 'Command description'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--create', type=str, help='Create evolution chain and respectives pokemons with ID of evolution chain. | Example: --create 1')
        parser.add_argument('-s', '--search', type=str, help='Get pokemons info (Name,Base stats,Height,Weight,Pokemon Id, Evolutions ) from evolution chain ID . | Example: --search 1')
        #parser.add_argument('-a3', '--argument3', type=str, help='info argument')
        

    def handle(self, *args, **kwargs):
        argument1= kwargs['create']
        argument2= kwargs['search']
       # argument3= kwargs['argument3']
        if  argument1:
            create=Create_pokemon(argument1)
        
        