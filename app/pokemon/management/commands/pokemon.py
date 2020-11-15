from django.core.management.base import BaseCommand
from ...views import Create_get_pokemon

class Command(BaseCommand):
    help = 'Command description'

    def add_arguments(self, parser):
        parser.add_argument('-c', '--create', type=str, help='Create evolution chain and respectives pokemons with ID of evolution chain. | Example: --create 1')
        parser.add_argument('-s', '--search', type=str, help='Get pokemons info (Name,Base stats,Height,Weight,Pokemon Id, Evolutions ) from evolution chain ID . | Example: --search 1')
        #parser.add_argument('-a3', '--argument3', type=str, help='info argument')
        

    def handle(self, *args, **kwargs):
        create= kwargs['create']
        search= kwargs['search']
       # argument3= kwargs['argument3']
        if  create:
            print(f'Creating evolution chain and respective pokemons with Evolution Chain ID : {create}')
            create=Create_get_pokemon(create, True)

        if  search:
            print(f'Searching evolution chain and respective pokemons with Evolution Chain ID : {search}')
            create=Create_get_pokemon(search, False)
        
        