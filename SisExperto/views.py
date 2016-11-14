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
				m = cantidad.count(enfermedad[i])
		if isinstance(text, SintomaEnfermedad):
			return str(text.enfermedad)
		else:
			return str(text)



'''
class ExpertoView(FormView):
	template_name = "SisExperto.html"
	form_class = FormExpert
	success_url = 'SisExperto'

	def __init__(self):
		self.text = ""
		self.cantidad = []
		self.lista_enfer = []	

	def form_valid(self, form):
		#This method is calle when valid for data has been POSTED
		#It should return an HttpResponse
		selecciones = form.cleaned_data['Seleccione_sintomas'] #guarda los sintomas seleccionados por el usuario
		self.cantidad = []
		for s in selecciones:
			self.lista_enfer = SintomaEnfermedad.objects.filter(sintoma=s)
			for e in self.lista_enfer:
				text = str(e.enfermedad)
				self.cantidad.append(text)
		#print self.mayor_probabilidad(self.lista_enfer, self.cantidad)
		self.get_context_data()
		#el siguiente return es obligatorio
		return super(ExpertoView, self).form_valid(form)

	def mayor_probabilidad(self, enfermedad, cantidad):
		m = -9999999
		text = ""
		for i in range(len(enfermedad)):
			if cantidad.count(enfermedad[i]) > m:
				text = enfermedad[i]
				m = cantidad.count(enfermedad[i])
		if isinstance(text, SintomaEnfermedad):
			return str(text.enfermedad)
		else:
			return str(text)

	def get_context_data(self, **kwargs):
		context = super(ExpertoView, self).get_context_data(**kwargs)
		context['enfermedad'] = self.mayor_probabilidad(self.lista_enfer, self.cantidad)
		return context
		#Falta enviar la enfermedad al html
'''