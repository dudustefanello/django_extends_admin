from django.db import models

class NumericModel(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.descricao
