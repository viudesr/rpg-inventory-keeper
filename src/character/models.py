from django.db import models


class BodyPart(models.Model):
    name = models.CharField("nom", max_length=200)
