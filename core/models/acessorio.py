from django.db import models


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"id:{self.id}, descrição:{self.descricao}"