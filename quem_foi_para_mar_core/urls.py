from django.urls import path
from . import views
from .views import PescadorViewSet, EmbarcacaoViewSet, ViagemViewSet, ContatoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"pescador", PescadorViewSet)
router.register(r"embarcacao", EmbarcacaoViewSet)
router.register(r"viagem", ViagemViewSet)
router.register(r"contato", ContatoViewSet)


urlpatterns = [
    path('', views.ViagemViewSet.list_barcos, name='list_barcos'),
    path('pescador/', views.PescadorViewSet),
    path('embarcacao/', views.EmbarcacaoViewSet),
    path('viagem/', views.ViagemViewSet),
    path('contato/', views.ContatoViewSet),
    path('detalhe_viagem/<int:pk>', views.ViagemViewSet.post_detail, name="post_detail"),
    path('criar_viagem/', views.ViagemViewSet.criar_viagem, name='criar_viagem'),

]
