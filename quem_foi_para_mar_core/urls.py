from django.urls import path
from . import views
from .views import UserViewSet, PescadorViewSet, EmbarcacaoViewSet, ViagemViewSet, ContatoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"pescador", PescadorViewSet)
router.register(r"embarcacao", EmbarcacaoViewSet)
router.register(r"viagem", ViagemViewSet)
router.register(r"contato", ContatoViewSet)


urlpatterns = [
    path('', views.ViagemViewSet.lista_barcos, name='lista_barcos'),
    path('pescador/', views.PescadorViewSet),
    path('embarcacao/', views.EmbarcacaoViewSet),
    path('viagem/', views.ViagemViewSet),
    path('contato/', views.ContatoViewSet),
    path('criar_viagem/', views.ViagemViewSet.criar_viagem, name='criar_viagem'),
    path('detalhe_viagem/<int:pk>', views.ViagemViewSet.detalhes_viagem, name="detalhes_viagem"),
    path('criar_pescador/', views.PescadorViewSet.criar_pescador, name="criar_pescador"),
    path('detalhe_pescador/<int:pk>', views.PescadorViewSet.detalhes_pescador, name="detalhes_pescador"),
    path('users/', views.UserViewSet),

]
