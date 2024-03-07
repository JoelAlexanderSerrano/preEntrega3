from django.shortcuts import render
from .models import DirectorTecnico
from .forms import DirectorTecnicoFormulario


def agregar_directortenico(request):

    if request.method == "POST":

        formulario = DirectorTecnicoFormulario(request.POST)

        if formulario.is_valid():

            info_dict = formulario.cleaned_data

            nuevo_dt = DirectorTecnico(nombre= info_dict["nombre"],
                                       apellido= info_dict["apellido"],
                                       edad= info_dict["edad"])
            
            nuevo_dt.save()

    else:

        formulario = DirectorTecnicoFormulario()        
    
    return render(request, "AppCuerpoTecnico/nuevo_dt.html", {"form":formulario})

def agregar_ayudantecampo(request):
    
    return render(request, "AppCuerpoTecnico/nuevo_ac.html")

def agregar_preparadorfisico(request):
    
    return render(request, "AppCuerpoTecnico/nuevo_pf.html")

def agregar_entrenadorarqueros(request):
    return render(request, "AppCuerpoTecnico/nuevo_ea.html")

def agregar_kinesiologo(request):
    
    return render(request, "AppCuerpoTecnico/nuevo_ki.html")
