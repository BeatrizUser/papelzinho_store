from rest_framework import serializers
from .models import Produto, ListaPresente

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ListaPresenteSerializer(serializers.ModelSerializer):
    produtos = ProdutoSerializer(many=True)

    class Meta:
        model = ListaPresente
        fields = '__all__'
