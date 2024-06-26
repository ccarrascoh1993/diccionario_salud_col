from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diccionario/', views.lista_terminos, name='lista_terminos'),
    #path('agregar/', views.agregar_termino, name='agregar_termino'),
    #path('editar/<int:termino_id>/', views.editar_termino, name='editar_termino'),
    #path('eliminar/<int:termino_id>/', views.eliminar_termino, name='eliminar_termino'),
]
