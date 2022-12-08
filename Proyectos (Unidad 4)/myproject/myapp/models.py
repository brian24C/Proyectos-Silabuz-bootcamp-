from django.db import models


class Proyecto(models.Model):
    titulo=models.CharField(max_length=400)
    foto=models.ImageField()
    descripcion=models.CharField(max_length=400)
    tag=models.CharField(max_length=400)
    url=models.CharField(max_length=400)






