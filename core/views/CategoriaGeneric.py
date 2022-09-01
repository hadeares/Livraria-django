"""from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Categoria
from core.serealizers import CategoriaSerializer



class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class  = CategoriaSerializer

class CategoriasDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class  = CategoriaSerializer"""