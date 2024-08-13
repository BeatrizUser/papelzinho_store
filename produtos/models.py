from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    link_afiliado = models.URLField(max_length=500)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class ListaPresente(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    produtos = models.ManyToManyField(Produto, related_name='listas_presentes')

    def __str__(self):
        return self.nome
