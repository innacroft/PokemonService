import requests
from .models import Pokemon, Evolution



class Create_pokemon:
    def __init__(self, id_): 
        self.id = id_
        self.create_pokemons_by_evolution()
        
    def create_pokemons_by_evolution(self):
    #    https://pokeapi.co/api/v2/evolution-chain
        url='https://pokeapi.co/api/v2/evolution-chain/'+str(self.id) +'/'
        response = requests.get(url)
        self.name_list=[]
        if response.status_code == 200:
            data=response.json()
            self.chain_id=data['id']
            Evolution.objects.get_or_create(id=self.chain_id)
            self.recursive_(data['chain'])  #get all info of each evolution including names of each pokemon
            self.get_pokemon_data(self.name_list) #get data of each pokemon by name
            return response.json()

    def recursive_(self,values):
        for key, value in values.items():
            if key=='species':
                name=[ v for k, v in value.items() if k == 'name']
                self.name_list.insert(0,name[0])
            if key=='evolves_to':
                for val1 in value:
                    self.recursive_(val1)
    
    def get_pokemon_data(self, name_list):
        for value in self.name_list:
            url='https://pokeapi.co/api/v2/pokemon/'+str(value)+'/'
            response = requests.get(url)
            data=response.json()
            print('|||||||',data['id'],data['name'],'|||||||')
            for stat in data['stats']:
                s=stat['stat']
                print(s['name'],stat['base_stat'])

                    
   
        
    

                
    

def get_pokemons_by_evolution(id):
#    https://pokeapi.co/api/v2/evolution-chain
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

# def get_username(params={}):
#     response = generate_request('https://randomuser.me/api', params)
#     if response:
#        user = response.get('results')[0]
#        return user.get('name').get('first')

#     return ''"
