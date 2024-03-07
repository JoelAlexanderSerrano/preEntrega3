from django import forms


class DirectorTecnicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apeliido = forms.CharField(max_length=30)
    edad = forms.IntegerField()

    def __str__(self):
        return self.nombre

class AyudanteCampoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apeliido = forms.CharField(max_length=30)
    edad = forms.IntegerField()

    def __str__(self):
        return self.nombre

class PreparadorFisicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apeliido = forms.CharField(max_length=30)
    edad = forms.IntegerField() 

    def __str__(self):
        return self.nombre

class EntrenadorArquerosFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apeliido = forms.CharField(max_length=30)
    edad = forms.IntegerField()       

    def __str__(self):
        return self.nombre

class KinesiologoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apeliido = forms.CharField(max_length=30)
    edad = forms.IntegerField()    

    def __str__(self):
        return self.nombre