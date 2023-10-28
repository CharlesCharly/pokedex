from django.db import models

class Pokemon(models.Model):
    attack = models.IntegerField()
    classification = models.CharField(max_length=100)
    defense = models.IntegerField()
    height_m = models.FloatField(null=True)
    hp = models.IntegerField()
    japanese_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pokedex_number = models.IntegerField(unique=True)
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, null=True, blank=True)
    weight_kg = models.FloatField(null=True)
    generation = models.IntegerField()
    is_legendary = models.BooleanField()

    def __str__(self):
        return self.name
