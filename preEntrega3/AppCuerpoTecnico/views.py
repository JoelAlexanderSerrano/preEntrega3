from django.shortcuts import render
from .models import DirectorTecnico, AyudanteCampo, PreparadorFisico, EntrenadorArqueros, Kinesiologo
from .forms import DirectorTecnicoFormulario, AyudanteCampoFormulario, PreparadorFisicoFormulario, EntrenadorArquerosFormulario, KinesiologoFormulario


def agregar_directortecnico(request):

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
    
    if request.method == "POST":

        formulario = AyudanteCampoFormulario(request.POST)

        if formulario.is_valid():

            info_dict = formulario.cleaned_data

            nuevo_ac = AyudanteCampo(nombre= info_dict["nombre"],
                                       apellido= info_dict["apellido"],
                                       edad= info_dict["edad"])
            
            nuevo_ac.save()

    else:

        formulario = AyudanteCampoFormulario()    
    
    
    return render(request, "AppCuerpoTecnico/nuevo_ac.html", {"form":formulario})


def agregar_preparadorfisico(request):
    
    if request.method == "POST":
        
        formulario = PreparadorFisicoFormulario(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_pf = PreparadorFisico(nombre = info_dict["nombre"],  
                                        apellido = info_dict["apellido"],
                                        edad = info_dict["edad"])
            
            nuevo_pf.save()
            
    else:
        
        formulario = PreparadorFisicoFormulario()        
    
    return render(request, "AppCuerpoTecnico/nuevo_pf.html", {"form":formulario})

def agregar_entrenadorarqueros(request):

    if request.method == "POST":
        
        formulario = EntrenadorArquerosFormulario(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_ea = EntrenadorArqueros(nombre = info_dict["nombre"],  
                                        apellido = info_dict["apellido"],
                                        edad = info_dict["edad"])
            
            nuevo_ea.save()
            
    else:
        
        formulario = EntrenadorArquerosFormulario()        

    return render(request, "AppCuerpoTecnico/nuevo_ea.html", {"form":formulario})

def agregar_kinesiologo(request):
    
    if request.method == "POST":
        
        formulario = KinesiologoFormulario(request.POST)
        
        if formulario.is_valid():
            
            info_dict = formulario.cleaned_data
            
            nuevo_ki = Kinesiologo(nombre = info_dict["nombre"],  
                                        apellido = info_dict["apellido"],
                                        edad = info_dict["edad"])
            
            nuevo_ki.save()
            
    else:
        
        formulario = KinesiologoFormulario()  
    
    return render(request, "AppCuerpoTecnico/nuevo_ki.html", {"form":formulario})
