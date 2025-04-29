from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(default=0, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
   
    
    def __str__(self):
        return f"id: {self.id};"