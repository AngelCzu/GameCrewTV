from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sala(models.Model):
    nombreSala = models.CharField(max_length=100)  # Puedes ajustar la longitud máxima según tus necesidades

    def str(self):
        txt = "ID: {0}"
        return txt.format(self.nombreSala)
    