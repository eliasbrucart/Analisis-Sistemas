from django.db import models

#Nombre de tabla
class Prueba(models.Model):
    nombre = models.CharField(max_length=255)

    apellido = models.CharField(max_length=255)

    def __str__(self):
        pass