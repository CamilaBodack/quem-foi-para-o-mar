from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Viagem, Pescador


class CriarNovoUsuarioForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ('destino', 'data_partida', 'data_chegada_prevista',
                  'tripulacao', 'embarcacao_id', 'pescador_id')


class PescadorForm(forms.ModelForm):
    class Meta:
        model = Pescador
        fields = ('nome', 'endereco', 'telefone', 'email')
