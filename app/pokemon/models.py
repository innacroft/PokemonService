from django.db import models


class Pokemon(models.Model):
    """Pokemon info on database"""
    pokemon = models.IntegerField(primary_key=True)
    is_baby = models.BooleanField(default=False, verbose_name='Is a baby?')
    name = models.CharField(max_length=100, verbose_name="Pokemon name")
    hp = models.IntegerField(default=0,verbose_name="Hit points")
    weight = models.DecimalField(default=0,max_digits=10, decimal_places=4,verbose_name="Width points")
    height = models.DecimalField(default=0,max_digits=10, decimal_places=4,verbose_name="Height points")
    attack = models.IntegerField(default=0,verbose_name="Attack points")
    defense = models.IntegerField(default=0,verbose_name="Deffense points")
    special_attack = models.IntegerField(default=0,verbose_name="Special Attack points")
    special_defense = models.IntegerField(default=0,verbose_name="Special Deffense points")
    speed = models.IntegerField(default=0,verbose_name="Speed points")  

class Evolution(models.Model):
    """Evolution Chain for each pokemon"""
    id_chain=models.IntegerField(default=0,verbose_name="Evolution_chain")
    pokemon=models.ForeignKey(Pokemon, on_delete=models.CASCADE, default=0)
    evolves_to=models.IntegerField(default=0,verbose_name="ID next evolution")
    chain_evol=models.TextField(default='')




    
