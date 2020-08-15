from django.shortcuts import render
from rest_framework import viewsets
from django.utils import timezone
from .models import Pescador, Embarcacao, Viagem, Contato
from .serializers import (PescadorSerializer, EmbarcacaoSerializer,
                          ViagemSerializer, ContatoSerializer)
from rest_framework.decorators import api_view
from .forms import ViagemForm, PescadorForm, CriarNovoUsuarioForm
from django.shortcuts import redirect,  get_object_or_404
from django.contrib.auth import login


def cadastro(request):
    if request.method == "GET":
        return render(request, "quem_foi_para_mar_core/cadastro.html", {"form": CriarNovoUsuarioForm})
    elif request.method == "POST":
        form = CriarNovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "quem_foi_para_mar_core/index.html", {})


class PescadorViewSet(viewsets.ModelViewSet):
    queryset = Pescador.objects.all()
    serializer_class = PescadorSerializer

    @api_view(['GET', 'POST'])
    def criar_pescador(request):
        if request.method == "POST":
            form = PescadorForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('detalhes_pescador', pk=post.pk)
        else:
            form = PescadorForm()
            return render(request, 'quem_foi_para_mar_core/criar_pescador.html', {'form': form})

    @api_view(['GET'])
    def detalhes_pescador(request, pk):
        post = get_object_or_404(Viagem, pk=pk)
        return render(request, 'quem_foi_para_mar_core/detalhe_viagem.html', {'post': post})


class EmbarcacaoViewSet(viewsets.ModelViewSet):
    queryset = Embarcacao.objects.all()
    serializer_class = EmbarcacaoSerializer


class ViagemViewSet(viewsets.ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    @api_view(['GET', 'POST'])
    def criar_viagem(request):
        if request.method == "POST":
            form = ViagemForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('detalhes_viagem', pk=post.pk)
        else:
            form = ViagemForm()
        return render(request, 'quem_foi_para_mar_core/criar_viagem.html', {'form': form})

    def detalhes_viagem(request, pk):
        post = get_object_or_404(Viagem, pk=pk)
        return render(request, 'quem_foi_para_mar_core/detalhe_viagem.html', {'post': post})

    @api_view(['GET'])
    def lista_barcos(request):
        barcos_no_mar_hoje = Viagem.objects.filter(data_partida=timezone.now()).order_by('data_partida')
        return render(request, 'quem_foi_para_mar_core/index.html', {'barcos_no_mar_hoje': barcos_no_mar_hoje})


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
