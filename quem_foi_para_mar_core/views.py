from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.utils import timezone
from .models import Pescador, Embarcacao, Viagem, Contato
from .serializers import (PescadorSerializer, EmbarcacaoSerializer,
                          ViagemSerializer, ContatoSerializer)
from rest_framework import status
from rest_framework.decorators import api_view
from .forms import ViagemForm


class PescadorViewSet(viewsets.ModelViewSet):
    queryset = Pescador.objects.all()
    serializer_class = PescadorSerializer


class EmbarcacaoViewSet(viewsets.ModelViewSet):
    queryset = Embarcacao.objects.all()
    serializer_class = EmbarcacaoSerializer


class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    @api_view(['GET'])
    def list_barcos(request):
        barcos_no_mar_hoje = Viagem.objects.filter(data_partida=timezone.now()).order_by('data_partida')
        return render(request, 'quem_foi_para_mar_core/informativos.html', {'barcos_no_mar_hoje': barcos_no_mar_hoje})

    @api_view(['POST'])
    def criar_viagem(request):
        criar_viagem = ViagemForm()
        return render(request, 'quem_foi_para_mar_core/criar_viagem.html', {'criar_viagem': criar_viagem})


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
