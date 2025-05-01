from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio, blank=True)

    def __str__(self):
        return f"id: {self.id}; modelo: {self.modelo}; cor: {self.cor}; ano: {self.ano}"
