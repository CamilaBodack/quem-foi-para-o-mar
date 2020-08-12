from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_barcos, name='Listar barcos'),
]
