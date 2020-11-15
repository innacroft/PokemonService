import requests
from .models import Pokemon, Evolution
from prettytable import PrettyTable



class Create_get_pokemon:
    """
    Create or Show pokemons and evolution 
    chain depends of create status
    on True create  pokemons and evolutions chain on db
    on False only show pokemosn and evolutions chain on console
    """

    def __init__(self, id_, create): 
        self.id = id_
        self.create = create
        self.create_pokemons_by_evolution()
        
    def create_pokemons_by_evolution(self):
        url='https://pokeapi.co/api/v2/evolution-chain/'+str(self.id) +'/'
        response = requests.get(url)
        self.name_list=[]
        self.len=0
        self.val2=''
        self.count=0
        self.count2=0
        self.evolution={}
        self.items_=[]
        self.last_value=''
        self.val=[]
        self.t = PrettyTable(['Id', 'Name','HP', 'Weight','Height', 'Attack','Defense',
            'Special_attack','Special defense', 'Speed','Is Baby?',  'Id Chain evolution']) 
        self.t2 = PrettyTable(['Evolution list']) 
        if response.status_code == 200:
            data=response.json()
            self.chain_id=data['id'] #chain evolution
            self.recursive_(data['chain'],'')  #get all info of each evolution including names of each pokemon
            self.evol=''
            print(self.t)
            
            counter=0
            
            for key, val in self.evolution.items():
                self.evol=str(val).replace(',','--->').replace('[',' ').replace(']','').replace('\'','')
                self.t2.add_row([ self.evol ])
                self.val.append(val)
                counter+=1
            print(self.t2)
            
            ev=Evolution.objects.filter(id_chain=data['id'])
            for element in ev:
                element.chain_evol=self.evol
                element.save()
            
            
        else:
            print('--> Ops !, Something went wrong with request, Error No:',response.status_code)


    def recursive_(self,values,before_value):
        
        for key, value in values.items():
            self.is_baby=False

            if key=='evolution_details':
                pass
            if key=='evolves_to':
                self.len=len(value)
                self.val2=value
            if key=='species':
                id_=self.get_save_data_pokemon(value['name'])
                self.insert_dependencies(id_,before_value)
                if len(self.items_) > 0:
                    length= len(self.items_)
                    self.last_value=str(self.items_[-1])
                if self.last_value == before_value:
                    self.items_.append(value['name'])
                    self.evolution[str(self.count2)]=self.items_ 
                else:
                    new_items=self.items_.copy()
                    new_items.pop()
                    new_items.append(value['name'])
                    self.evolution[str(self.count2)+str(self.count2)]=new_items
                    self.count2+=1
                self.count+=1
                
        if self.len != 0:
            for val1 in self.val2:
                self.recursive_(val1,before_value=value['name'])

    def insert_dependencies(self, id_, before_value): #dependencies of pokemon evolutions
        if self.create:
            if before_value:
                id_pok=Pokemon.objects.get(name=before_value)  
                Evolution.objects.get_or_create(id_chain=self.chain_id,pokemon=id_pok,evolves_to=id_)

    def get_save_data_pokemon(self, name_pokemon):
        
        hp,attack,defense,special_attack,special_defense,speed=0,0,0,0,0,0
        width,weight=0.0,0.0
        is_baby_=False
        index_=-1
        name,baby= '',''
        
        url='https://pokeapi.co/api/v2/pokemon/'+str(name_pokemon)+'/'
        response = requests.get(url)
        data=response.json()
        if data['weight']: weight = data['weight']/10
        if data['height']: height = data['height']/10
        for stat in data['stats']:
            s=stat['stat']
            name=data['name'] 
            id_=data['id']
            if s['name']=='hp': hp = stat['base_stat'] 
            if s['name']=='attack': attack = stat['base_stat']
            if s['name']=='defense': defense = stat['base_stat']
            if s['name']=='special-attack': special_attack = stat['base_stat']
            if s['name']=='special-defense': special_defense = stat['base_stat']
            if s['name']=='speed': speed = stat['base_stat']
        if self.count==0:
            is_baby_=True
            baby='Yes'
        else:
            is_baby_=False
            baby='No'
        if self.create:
            Pokemon.objects.get_or_create(pokemon=id_, 
            is_baby=is_baby_, name= name, hp=hp, 
            attack=attack,weight=weight, height=height,
            defense=defense,speed=speed, special_attack=special_attack, 
            special_defense=special_defense)
        else:
            pass
        self.t.add_row([id_,name,hp,str(weight)+ ' kg',str(height)+' m',attack,defense,special_attack,special_defense,speed,baby,self.chain_id])
        return id_






