import requests
from .models import Pokemon, Evolution
from prettytable import PrettyTable



class Create_get_pokemon:

    def __init__(self, id_, create): 
        self.id = id_
        self.create = create
        self.create_pokemons_by_evolution()
        
    def create_pokemons_by_evolution(self):
        url='https://pokeapi.co/api/v2/evolution-chain/'+str(self.id) +'/'
        response = requests.get(url)
        self.name_list=[]
        if response.status_code == 200:
            data=response.json()
            self.chain_id=data['id']
            Evolution.objects.get_or_create(id=self.chain_id)
            self.recursive_(data['chain'])  #get all info of each evolution including names of each pokemon
            self.get_pokemon_data(self.name_list) #get data of each pokemon by name and save it
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
        hp=0
        attack=0
        defense=0
        special_attack=0
        special_defense=0
        speed=0.0
        width=0.0
        weight=0
        is_baby_=False
        index_=-1
        name= ''
        baby=''

        t = PrettyTable(['Id', 'Name','HP', 'Weight','Height', 'Attack','Defense',
            'Special_attack','Special defense', 'Speed','Is Baby?', 'Evolution', 'Id Chain evolution'])
        for value in self.name_list:
            url='https://pokeapi.co/api/v2/pokemon/'+str(value)+'/'
            response = requests.get(url)
            data=response.json()
            
            if data['weight']:
                weight = data['weight']/10
            if data['height']:
                height = data['height']/10
            for stat in data['stats']:
                s=stat['stat']
                name=data['name'] 
                id_=data['id']
                if s['name']=='hp':
                    hp = stat['base_stat'] 
                if s['name']=='attack':
                    attack = stat['base_stat']
                if s['name']=='defense':
                    defense = stat['base_stat']
                if s['name']=='special-attack':
                    special_attack = stat['base_stat']
                if s['name']=='special-defense':
                    special_defense = stat['base_stat']
                if s['name']=='speed':
                    speed = stat['base_stat']
                

            index_=self.name_list.index(name)

            if index_ == 0:
                is_baby_=True
                baby='Yes'
            else:
                is_baby_=False
                baby='No'
            evol=str(self.name_list).replace(',','--->').replace('[',' ').replace(']','').replace('\'','')
            if self.create:
                obj= Evolution.objects.get(pk =self.chain_id )
                try:
                    Pokemon.objects.get(pokemon=id_).delete()
                    
                except Exception as e:
                    Pokemon.objects.get_or_create(pokemon=id_,evolution=obj,
                        order=index_,is_baby=is_baby_, name= name, hp=hp, attack=attack,weight=weight, height=height,
                        defense=defense,speed=speed, special_attack=special_attack, special_defense=special_defense,evolution_graph=evol)
            else:
                pass
            t.add_row([id_,name,hp,str(weight)+ ' kg',str(height)+' m',attack,defense,special_attack,special_defense,speed,baby,evol,self.chain_id])
        print(t)



