from django import forms

class CrearDjuserForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField(required=False)
    email = forms.CharField(max_length=30)

class RegArtistForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    nomre_art = forms.CharField(max_length=40)
    fecha_nacimiento = forms.DateField(required=False)

class RegTrackForm(forms.Form):
    trackid = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=100)
    fecha_lanzamiento = forms.DateField(required=False)