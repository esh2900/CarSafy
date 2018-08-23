from django.http import HttpResponse
from django.shortcuts import render

def perguntas_frequentes(request):
    return render(request, "faq.html")

def contato (request):
    return render(request, "contato.html")

def cotacao (request):
    return render(request, "cotacao.html")