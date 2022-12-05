from django.db import models
import datetime
class familiar(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100, null=False)
    edad = models.IntegerField(null=False)
    fecha_nacimiento = models.DateField(null=False)
    
    @classmethod
    def create (self,nombre:str, edad:int ,fecha_nacimiento: datetime.date):
        return self(nombre=nombre, edad=edad, fecha_nacimiento=fecha_nacimiento)