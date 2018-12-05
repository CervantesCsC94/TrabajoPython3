from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.



class Categoria(models.Model):
	categoria=models.CharField(max_length=50)	

	def __str__(self):
		return self.categoria		


class Critica(models.Model):
	user=models.CharField(max_length=100)
	titulo=models.CharField(max_length=100)
	categoria=models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	timestap=models.DateTimeField(auto_now_add=True)
	contenido=models.TextField(blank=True)
	calificacion=models.IntegerField(null=True, blank=True)
	
	
	def __str__(self):
		return self.titulo
