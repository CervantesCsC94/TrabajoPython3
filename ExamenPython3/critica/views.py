from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Critica,Categoria

# Create your views here.

class Categorias(generic.ListView):
	model=Categoria
	template_name="critica/categorias.html"

def lista_criticas(request,id=1):
	queryset1=Categoria.objects.get(id=id)	
	queryset2=Critica.objects.all()
	contex={"categoria":queryset1,"criticas":queryset2}
	return render(request,"critica/listaCriticas.html",contex)

class CrearCritica(generic.CreateView):
	template_name="critica/crear.html"
	model=Critica
	fields=["user","titulo",'categoria','contenido']
	success_url='/categorias'

class DetailCritica(generic.DetailView):
	template_name="critica/detail_critica.html"
	model=Critica