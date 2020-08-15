from rest_framework import serializers
from .models import Pescador, Embarcacao, Viagem, Contato, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nome", "email", "senha")


class PescadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pescador
        fields = ("nome", "endereco", "telefone", "email")


class EmbarcacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Embarcacao
        fields = ("nome", "numeracao", "modelo", "caracteristicas")


class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = ("destino", "data_partida", "data_chegada_prevista",
                  "tripulacao", "embarcacao_retornou")


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = ("nome", "endereco", "email", "telefone")
