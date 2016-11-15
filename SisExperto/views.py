from django.shortcuts import render
from .Forms import FormExpert
from django.views.generic.edit import FormView
from .models import Enfermedad, Sintoma, SintomaEnfermedad

def ExpertoView(request):
	form = FormExpert(request.POST or None)
	context = {
		'form': form,
	}
	if form.is_valid():
		selecciones = form.cleaned_data['Seleccione_sintomas'] #guarda los sintomas seleccionados por el usuario
		cantidad = []
		for s in selecciones:
			lista_enfer = SintomaEnfermedad.objects.filter(sintoma=s)
			for e in lista_enfer:
				text = str(e.enfermedad)
				cantidad.append(text)
		enfer = mayor_probabilidad(lista_enfer, cantidad)
		objEnfermedad = Enfermedad.objects.filter(nombre=enfer)
		if len(objEnfermedad) > 0:
		    e = objEnfermedad[0].nombre
    		tratamiento = objEnfermedad[0].tratamiento
		context = {
			'enfermedad': e,
			'tratamiento': tratamiento,
		}
	return render(request, 'SisExperto.html', context)

def mayor_probabilidad(enfermedad, cantidad):
		m = -9999999
		text = ""
		for i in range(len(enfermedad)):
			if cantidad.count(enfermedad[i]) > m:
				text = enfermedad[i]
				print text
				m = cantidad.count(enfermedad[i])
		if isinstance(text, SintomaEnfermedad):
			return str(text.enfermedad)
		else:
			return str(text)