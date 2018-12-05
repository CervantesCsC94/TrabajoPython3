from django.contrib import admin
from django.urls import path

from critica import views
from django.contrib.auth import views as auth_view



app_name="critica"

urlpatterns = [
    
    path('',auth_view.LoginView.as_view(template_name="critica/login.html"),name='login'),
    path('categorias/',views.Categorias.as_view(),name="categorias_view"),
    path('criticas/<int:id>',views.lista_criticas,name='criticas_view'),
    path('crear/',views.CrearCritica.as_view(),name="crear_view"),
    path('critca/<int:pk>',views.DetailCritica.as_view(), name='detail_view'),

]
