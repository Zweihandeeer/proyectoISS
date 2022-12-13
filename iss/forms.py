from dataclasses import field
from iss.models import Cartas, Observaciones
from django import forms
from django.forms import ModelForm

# Formulario de inicio de sesión.
class LoginForm(forms.Form):
    usuario = forms.CharField(
        max_length=250, min_length=3, label='Ingrese su nombre de usuario')
    password = forms.CharField(min_length=8, max_length=16,
                               label='Ingrese su contraseña', widget=forms.PasswordInput())

class ObservacionesForm(forms.Form):
    class Meta:
        model: Observaciones
        fields = ['nombrejugador','fecha_creacion', 'actividad', 'observacion']

# Formulario de muestreo de la tabla de cartas
class CartasForm(ModelForm):
    class Meta:
        model = Cartas
        fields =['idbiblioteca','juego','sets','idcarta','nombrecarta','habilidad','keyword','costomana','fuerza','salud', 'rareza','tipocarta','region','tipohechizo']
        labels = {
            'idbiblioteca':'ID de biblioteca',
            'juego':'Juego',
            'sets':'Sets:',
            'idcarta':'ID de carta',
            'nombrecarta':'Nombre',
            'habilidad':'Habilidad',
            'keyword':'Keyword',
            'costomana':'Costo de mana',
            'fuerza':'Fuerza',
            'salud':'Salud',
            'rareza':'Rareza',
            'tipocarta':'Tipo de carta',
            'region':'Region',
            'tipohechizo':'Tipo de hechizo',
            }
        widgets={
            'idbiblioteca':forms.NumberInput(attrs={'class':'form-control'}),
            'juego':forms.Textarea(attrs={'class':'form-control'}),
            'sets':forms.Textarea(attrs={'class':'form-select'}),
            'idcarta':forms.NumberInput(attrs={'class':'form-control'}),
            'nombrecarta':forms.TextInput(attrs={'class':'form-control'}),
            'habilidad':forms.TextInput(attrs={'class':'form-control'}),
            'keyword':forms.TextInput(attrs={'class':'form-control'}),
            'costomana':forms.TextInput(attrs={'class':'form-control'}),
            'fuerza':forms.NumberInput(attrs={'class':'form-control'}),
            'salud':forms.NumberInput(attrs={'class':'form-control'}),
            'rareza':forms.NumberInput(attrs={'class':'form-control'}),
            'tipocarta':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
            'tipohechizo':forms.TextInput(attrs={'class':'form-control'}),
        }