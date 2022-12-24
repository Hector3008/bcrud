from django import forms
from bcrud.models import *

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    rate = forms.IntegerField()
    descripcion=forms.CharField()