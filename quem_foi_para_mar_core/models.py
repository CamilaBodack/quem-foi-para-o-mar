from django.db import models


class Pescador(models.Model):
    nome = models.CharField("Nome", max_length=254)
    endereco = models.CharField("Endereço", max_length=254)
    telefone = models.CharField("Telefone", max_length=50)
    email = models.EmailField("Email")

    def __str__(self):
        return self.nome


class Embarcacao(models.Model):
    nome = models.CharField("Nome", max_length=254)
    numeracao = models.CharField("Numeração", max_length=50)
    modelo = models.CharField("Modelo", max_length=100)
    caracteristicas = models.CharField("características", max_length=254)

    def __str__(self):
        return self.nome


class Viagem(models.Model):
    destino = models.CharField("Destino", max_length=254)
    data_partida = models.DateField("Data de partida", auto_now=False)
    data_chegada_prevista = models.DateField("Data de chegada prevista", auto_now=False)
    tripulacao = models.CharField("Nome dos tripulantes", max_length=254)
    embarcacao_retornou = models.BooleanField("Retornou ?", default=False)
    pescador_id = models.ForeignKey(Pescador, on_delete=models.PROTECT)
    embarcacao_id = models.ForeignKey(Embarcacao, on_delete=models.PROTECT)

    def __str__(self):
        return self.destino


class Contato(models.Model):
    nome = models.CharField("Nome", max_length=254)
    endereco = models.CharField("Endereço", max_length=254)
    email = models.EmailField("E-mail")
    telefone = models.CharField("Telefone", max_length=50)

    def __str__(self):
        return self.nome
