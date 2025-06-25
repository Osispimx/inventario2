from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Categoria

@login_required
def mis_categorias(request):
    categorias = request.user.categorias.all()
    return render(request, 'lista_categorias/categorias.html', {
        'categorias': categorias
    })
