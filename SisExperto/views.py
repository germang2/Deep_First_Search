from django.shortcuts import render
from .Forms import FormExpert
#from .expert import fileToStr
from django.views.generic.edit import FormView
from .models import Enfermedad, Sintoma, SintomaEnfermedad

class ExpertoView(FormView):
	template_name = "SisExperto.html"
	form_class = FormExpert
	success_url = 'SisExperto'
	

	def form_valid(self, form):
		#This method is calle when valid for data has been POSTED
		#It should return an HttpResponse
		selecciones = form.cleaned_data['Seleccione_sintomas'] #guarda los sintomas seleccionados por el usuario
		cantidad = []
		for s in selecciones:
			lista_enfer = SintomaEnfermedad.objects.filter(sintoma=s)
			for e in lista_enfer:
				text = str(e.enfermedad)
				cantidad.append(text)
		print self.mayor(lista_enfer, cantidad)
		#FALTA TERMINAR
		#Falta comparar y encontrar la enfermedad que se repite mas veces

		#el siguiente return es obligatorio
		return super(ExpertoView, self).form_valid(form)

	def mayor(self, enfermedad, cantidad):
		m = -9999999
		text = ""
		for i in range(len(enfermedad)):
			if cantidad.count(enfermedad[i]) > m:
				text = enfermedad[i]
				m = cantidad.count(enfermedad[i])
		return str(text.enfermedad)