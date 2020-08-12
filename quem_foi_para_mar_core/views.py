from django.shortcuts import render
from .models import Pescador, Embarcacao, Viagem, Contato


def list_barcos(request):
    return render(request, 'quem_foi_para_mar_core/geral.html', {})
