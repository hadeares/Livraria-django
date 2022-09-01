from rest_framework import ModelSerializer
from core.models import Categoria 


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'