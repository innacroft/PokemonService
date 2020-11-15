# POKEMON API INTEGRATION
Consumed Pokemon API avaliable on  https://pokeapi.co/docs/v2 
This application creates and shows avaliable Pokemons grouped by Pokemon Evolution Chain, gets main details for each Pokemon and shows evolution chains for each Pokemon via console on python-django.

## Technologies:
 - Postgresql 
 - Docker
 -  Python
 - Gunicorn
 - Django-rest-framework
 - Celery
 
## Features
On console using django custom command, shows name, base stats( Hp, Weight, Height, Attack, Deffense, Special attack ,Special deffense  and Speed), related  to any Pokemon, adittionally shows Evolution representation graphically , Id chain evolution and show if a Pokemon is a baby or not. 
 
The command created on django application is **pokemons** and recieve 2 parameters : the **main action** (create or search) and the **ID** of Evolution Chain (see Evolution Chains on https://pokeapi.co/docs/v2 ).

-Command **create** -->create pokemons related to an specific Evolution Chain on local database , adittionally created data is showed on command line:

> python manage.py  **pokemons  --create ID**

-Command **search** --> show pokemons related to an specific Evolution Chain, show same information as create command but doesn't create anything on database:
> python manage.py  **pokemons  --search ID**

*Output sample:
|Id |    Name   | HP |  Weight  | Height | Attack | Defense | Special_attack | Special defense | Speed | Is Baby? |   Evolution | Id Chain evolution 
|--|--|--|--|--|--|--|--|--|--|--|--|--|
| 172 |  pichu  | 20 |  2.0 kg | 0.3 m  |   40   |    15   |       35       |        35       |   60  |   Yes    |  pichu---> pikachu---> raichu |         10         |
|  25 | pikachu | 35 |  6.0 kg | 0.4 m  |   55   |    40   |       50       |        50       |   90  |    No    |  pichu---> pikachu---> raichu |         10         |
|  26 |  raichu | 60 | 30.0 kg | 0.8 m  |   90   |    55   |       90       |        80       |  110  |    No    |  pichu---> pikachu---> raichu |         10         |

|Evolution list |
|--|
|pichu---> pikachu---> raichu|




