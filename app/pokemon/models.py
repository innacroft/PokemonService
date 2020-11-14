from django.db import models

class Evolution(models.Model):
    """Evolution Chain for each pokemon"""
    id = models.AutoField(primary_key=True)

class Pokemon(models.Model):
    """Pokemon info on database"""
    pokemon = models.IntegerField(primary_key=True)
    evolution=models.ForeignKey(Evolution, on_delete=models.CASCADE)
    order = models.IntegerField(default=0,verbose_name="Order of evolution if have one")
    is_baby = models.BooleanField( verbose_name='Is a baby?')
    name = models.CharField(max_length=100, verbose_name="Pokemon name")
    hp = models.IntegerField(verbose_name="Hit points")
    attack = models.IntegerField(verbose_name="Attack points")
    deffense = models.IntegerField(verbose_name="Deffense points")
    special_attack = models.IntegerField(verbose_name="Special Attack points")
    special_deffense = models.IntegerField(verbose_name="Special Deffense points")
    speed = models.IntegerField(verbose_name="Speed points")
    
    
    




    
