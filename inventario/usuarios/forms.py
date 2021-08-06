from .models import Escritor,Libro
from django.forms import ModelForm

class AutorForm(ModelForm):
    class Meta:
        model=Escritor
        fields='__all__'
#fields=['nombre','correo']

class LibroForm(ModelForm):
    class Meta:
        model=Libro
        fields='__all__'
