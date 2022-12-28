from django.db import models
from registro.models import Pais

# Create your models here.

class ReporteBase(models.Model): 

    archivo      = models.CharField(('archivo'), max_length=255)
    creacion     = models.DateTimeField(('creacion'), auto_now=True)
    semana       = models.IntegerField(('semana'),)
    fecha_inicio = models.DateTimeField(('fecha_inicio'), blank=True, null=True)
    fecha_fin    = models.DateTimeField(('fecha_fin'), blank=True, null=True)

class Informe(models.Model):

    ESTADO =(
        ('1','Iniciando'),('2','Procesando'),('3','Procesado'),('4','Error')
    )    


    pais         = models.ForeignKey(Pais,on_delete=models.CASCADE)
    nombre       = models.CharField(('nombre'), max_length=50)
    descripcion  = models.TextField(('descripcion'),blank=True, null=True)
    fecha_inicio = models.DateTimeField(('fecha_inicio'), auto_now=True)
    fecha_fin    = models.DateTimeField(('fecha_fin'), blank=True, null=True)
    estado       = models.CharField(max_length=1, choices=ESTADO )
    reportes     = models.ManyToManyField(ReporteBase, blank=True)



class Grafica(models.Model):

    ARCHIVO =(
        ('1','png'),
        ('2','jpg'),

    )

    informe      = models.ForeignKey(Informe, null=True, blank=True, on_delete=models.CASCADE)
    archivo      = models.CharField(('archivo'), max_length=1, choices=ARCHIVO)



