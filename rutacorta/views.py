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
			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/A-C.jpg'
			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/A-D.jpg'	
			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/A-E.jpg'
			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'B':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/B-A.jpg'
			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/B-C.jpg'
			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/B-D.jpg'	
			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/B-E.jpg'
			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'C':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/C-A.jpg'
			elif ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/C-B.jpg'
			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/C-D.jpg'	
			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/C-E.jpg'
			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'E':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/E-A.jpg'
			elif ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/E-B.jpg'
			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/E-C.jpg'	
			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/E-D.jpg'
			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'D':
			
			imagen = 'static/grafos/D-Cualquiera.jpg'
			
		context['ruta'] = imagen

	return render(request, 'rutacorta.html', context)