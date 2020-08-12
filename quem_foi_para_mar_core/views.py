from django.shortcuts import render


def list_barcos(request):
    return render(request, 'quem_foi_para_mar_core/list_barcos.html', {})
