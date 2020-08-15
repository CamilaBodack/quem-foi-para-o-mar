from django import forms
from .models import Viagem, Pescador


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ('destino', 'data_partida', 'data_chegada_prevista',
                  'tripulacao', 'embarcacao_id', 'pescador_id')


class PescadorForm(forms.ModelForm):
    class Meta:
        model = Pescador
        fields = ('nome', 'endereco', 'telefone', 'email')
