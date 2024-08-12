from django import forms
from .models import MiModelo

class MiFormulario(forms.ModelForm):
    campo1 = forms.CharField(max_length=50)
    campo2 = forms.IntegerField(min_value=0)
    
    def clean_campo1(self):
        valor = self.cleaned_data['campo1']
        if valor == 'prohibido':
            raise forms.ValidationError("No se permite el valor 'prohibido'")
        return valor

    class Meta:
        model = MiModelo
        fields = ['campo1', 'campo2', 'campo3']

from .models import HorarioClase

class HorarioClaseForm(forms.ModelForm):
    class Meta:
        model = HorarioClase
        fields = '__all__'

from django.forms.widgets import Textarea
from .models import HorarioClase

class HorarioClaseForm(forms.ModelForm):
    class Meta:
        model = HorarioClase
        fields = '__all__'
        widgets = {
            'horarios': Textarea(attrs={'class': 'table'}),
        }