from django.db import models
from character.models import BodyPart


class Ammunition(models.Model):
    name = models.CharField("nom", max_length=200)
    quantity = models.IntegerField("quantité")
    weight = models.FloatField("poids")
    price = models.IntegerField("prix")
    rarity = models.IntegerField("rareté")


class Armor(models.Model):
    name = models.CharField("nom", max_length=200)
    physical_res = models.IntegerField("résistance ballistique")
    energy_res = models.IntegerField("résistance énergétique")
    radiation_res = models.IntegerField("résistance radiation")
    bodyparts = models.CharField("parties couvertes", max_length=200)
    weight = models.FloatField("poids")
    price = models.IntegerField("prix")
    rarity = models.IntegerField("rareté")


class Weapon(models.Model):
    name = models.CharField("nom", max_length=200)
    damage = models.IntegerField("dégâts")
    effect = models.CharField("effet", max_length=200)
    damage_type = models.CharField("type", max_length=200)
    rate = models.IntegerField("cadence")
    attack_range = models.CharField("portée", max_length=1)
    bonus = models.CharField("bonus", max_length=200)
    weight = models.FloatField("poids")
    price = models.IntegerField("prix")
    rarity = models.IntegerField("rareté")
    ammunition = models.ForeignKey(Ammunition, on_delete=models.CASCADE)