from django import forms
from .models import Veterinaria


class VeterinariaForm(forms.ModelForm):
    class Meta:
        model = Veterinaria
        fields = '__all__'
