from rest_framework import viewsets
from .models import Produto, ListaPresente
from .serializers import ProdutoSerializer, ListaPresenteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ListaPresenteViewSet(viewsets.ModelViewSet):
    queryset = ListaPresente.objects.all()
    serializer_class = ListaPresenteSerializer
