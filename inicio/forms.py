from django import forms

class CrearDjuserForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)

