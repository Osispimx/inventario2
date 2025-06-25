from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class categoria(models.Model):
    codigo=models.CharField(max_length=25)
    nombre=models.CharField(max_length=25)
    stock=models.PositiveIntegerField()
    detalles=models.CharField(max_length=500)
    usuarios = models.ManyToManyField(User, related_name='categorias')

    def __str__(self):
        return self.nombre