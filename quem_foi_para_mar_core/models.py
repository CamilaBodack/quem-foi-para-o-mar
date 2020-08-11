from django.db import models


class Pescador(models.Model):
    class Meta:
        verbose_name_plural = "Pescadores"

    nome = models.CharField("Nome", max_length=254)
    endereco = models.CharField("Endereço", max_length=254)
    telefone = models.CharField("Telefone", max_length=50)
    email = models.EmailField("Email")

    def __str__(self):
        return self.nome


class Embarcacao(models.Model):
    class Meta:
        verbose_name_plural = "Embarcações"
    nome = models.CharField("Nome", max_length=254)
    numeracao = models.CharField("Numeração", max_length=50)
    modelo = models.CharField("Modelo", max_length=100)
    caracteristicas = models.CharField("características", max_length=254)

    def __str__(self):
        return self.nome


class Viagem(models.Model):
    class Meta:
        verbose_name_plural = "Viagens"
    destino = models.CharField("Destino", max_length=254)
    data_partida = models.DateField("Data de partida", auto_now=False)
    data_chegada_prevista = models.DateField("Data de chegada prevista", auto_now=False)
    tripulacao = models.CharField("Nome dos tripulantes", max_length=254)
    embarcacao_retornou = models.BooleanField("Retornou ?", default=False)
    embarcacao_id = models.ForeignKey(Embarcacao, on_delete=models.PROTECT)
    pescador_id = models.ForeignKey(Pescador, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.destino


class Contato(models.Model):
    class Meta:
        verbose_name_plural = "Contatos"
    nome = models.CharField("Nome", max_length=254)
    endereco = models.CharField("Endereço", max_length=254)
    email = models.EmailField("E-mail")
    telefone = models.CharField("Telefone", max_length=50)
    pescador_id = models.ForeignKey(Pescador, default=0, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
