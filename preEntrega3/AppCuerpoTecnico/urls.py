from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio),
    path("nuevo_dt/", agregar_directortecnico),
    path("nuevo_ac/", agregar_ayudantecampo),
    path("nuevo_pf/", agregar_preparadorfisico),
    path("nuevo_ea/", agregar_entrenadorarqueros),
    path("nuevo_ki/", agregar_kinesiologo),
   

]