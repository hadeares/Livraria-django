from django.http import HttpResponse
from core.models import Categoria
from django.views import View

import json


class CategoriaView(View):
    def get(self, request):
        data = list(Categoria.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content="aplication/json")