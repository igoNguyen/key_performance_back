from django.db import models

# Create your models here.

class Pais(models.Model):

    ESTADO=(
        ('1','Iniciando'), ('2','Procesando'), ('3','Procesado'), ('4','Error')
    )

    pais        = models.CharField(max_length=50)
    nombre      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    estado      = models.CharField(max_length=1, choices=ESTADO)