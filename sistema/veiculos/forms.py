from django import forms
from veiculos.models import Veiculo

class FormularioVeiculo(forms.ModelForm):


    class Meta:
        model = Veiculo
        exclude = []

        