from django.shortcuts import render
from .Forms import FormExpert
#from .expert import fileToStr
from django.views.generic.edit import FormView

class ExpertoView(FormView):
	template_name = "SisExperto.html"
	form_class = FormExpert
	success_url = 'SisExperto'
	def __init__(self):
		self.arbol = eval(self.fileToStr('SisExperto/enfermedades.txt')) #evalua el archivo
		self.Nodoactual = self.arbol
		self.pregunta = self.Nodoactual[0]

	def form_valid(self, form):
		#This method is calle when valid for data has been POSTED
		#It should return an HttpResponse
		if len(self.Nodoactual) == 3:
			[self.pregunta, yesNode, noNode] = self.Nodoactual

			if form.is_valid(): 
				form_data = form.cleaned_data
				respuesta = form_data.get('campo')
		        if respuesta == 'y':
		        	self.Nodoactual = yesNode
		        else: 
		            self.Nodoactual = noNode
                self.pregunta = self.Nodoactual[0]

		#el siguiente return es obligatorio
		return super(ExpertoView, self).form_valid(form)

	def get_context_data(self, **kargs):
		""" Use this to add extra context """
		context = super(ExpertoView, self).get_context_data(**kargs)
		context["pregunta"] = self.pregunta
		return context

	def fileToStr(self, fileName): 
	    """Retorna la cadena que contiene el nombre del archivo."""
	    fin = open(fileName); 
	    contents = fin.read();  
	    fin.close() 
	    return contents


'''
def SisExperto(request):
	arbol = eval(fileToStr('SisExperto/enfermedades.txt')) #evalua el archivo
	form = FormExpert(request.POST or None)
	request.session["Nodoactual"] = arbol																																																																																															7	77u
	print request.session["bandera"]
	respuesta = None
	pregunta = None
	if len(request.session["Nodoactual"]) == 3:
		[pregunta, yesNode, noNode] = request.session["Nodoactual"]
		if form.is_valid(): 
			form_data = form.cleaned_data
			respuesta = form_data.get('campo')
	        if respuesta == 'y':
	        	request.session["Nodoactual"] = yesNode
	        else: 
	            request.session["Nodoactual"] = noNode
    	print request.session["Nodoactual"]
	context = {
		'form':form,
		'pregunta': pregunta,
	}
	return render(request, 'SisExperto.html', context)
'''
def fileToStr(fileName): 
    """Retorna la cadena que contiene el nombre del archivo."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents
