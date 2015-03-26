from django.shortcuts import render
from django.http import HttpResponse
from models import Pages


def handler(request, resource):
	fila = Pages.objects.filter(name=resource)
	if len(fila) == 0:
		fila = Pages(name=resource, page="Pagina de " + resource)
		fila.save()
		return HttpResponse(fila.page)
	else:
		return HttpResponse(fila[0].page)
