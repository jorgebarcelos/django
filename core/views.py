from multiprocessing import context
import re
from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Zé da Couve'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')