from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViagemViewSet.list_barcos, name='Listar barcos'),
]
