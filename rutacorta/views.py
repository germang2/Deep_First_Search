from django.shortcuts import render
from .form import RutaCorta
from .dijkstra import main

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
		camino = ""

		if ciudad_origen.capitalize() == 'A':
			if ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/A-B.jpg'
				camino = main('A','B')

			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/A-C.jpg'
				camino = main('A','C')

			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/A-D.jpg'	
				camino = main('A','D')

			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/A-E.jpg'
				camino = main('A','E')

			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'B':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/B-A.jpg'
				camino = main('B','A')

			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/B-C.jpg'
				camino = main('B','C')

			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/B-D.jpg'	
				camino = main('B','D')

			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/B-E.jpg'
				camino = main('B','E')

			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'C':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/C-A.jpg'
				camino = main('C','A')

			elif ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/C-B.jpg'
				camino = main('C','B')

			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/C-D.jpg'	
				camino = main('C','D')

			elif ciudad_destino.capitalize() == 'E':
				imagen = 'static/grafos/C-E.jpg'
				camino = main('C','E')

			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'E':
			if ciudad_destino.capitalize() == 'A':
				imagen = 'static/grafos/E-A.jpg'
				camino = main('E','A')

			elif ciudad_destino.capitalize() == 'B':
				imagen = 'static/grafos/E-B.jpg'
				camino = main('E','B')

			elif ciudad_destino.capitalize() == 'C':
				imagen = 'static/grafos/E-C.jpg'	
				camino = main('E','C')

			elif ciudad_destino.capitalize() == 'D':
				imagen = 'static/grafos/E-D.jpg'
				camino = main('E','D')

			else:
				imagen = 'static/grafos/invalido.jpeg'

		elif ciudad_origen.capitalize() == 'D':
			
			imagen = 'static/grafos/D-Cualquiera.jpg'
			camino = main('D','D')

		else:
			imagen = 'static/grafos/invalido.jpeg'

		context['ruta'] = imagen
		context['camino'] = camino

	return render(request, 'rutacorta.html', context)