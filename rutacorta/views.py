from django.shortcuts import render
from .form import RutaCorta

# Create your views here.
def rutacorta(request):
	form = RutaCorta(request.POST or None)
	context = {
		'form': form,
	}

	if form.is_valid():
		form_data = form.cleaned_data
		ciudad_origen = form_data.get('Ciudad_inicio')
		ciudad_destino = form_data.get('Ciudad_destino')
		if ciudad_origen.capitalize() == 'A':
			if ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/A-B.jpg'
			if ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/A-C.jpg'	
		context['ruta'] = imagen

	return render(request, 'rutacorta.html', context)