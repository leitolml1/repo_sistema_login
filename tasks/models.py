from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Taks(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    fecha_completada=models.DateTimeField(null=True)
    tarea_importante=models.BooleanField(default=False)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)