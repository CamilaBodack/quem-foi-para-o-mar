from django import forms
from .models import Viagem


class ViagemForm(forms.ModelForm):

    class Meta:
        model = Viagem
        fields = ('destino', 'data_partida', 'data_chegada_prevista',
                  'tripulacao', 'embarcacao_id', 'pescador_id')
