from django import forms
from .models import Sintoma

sintomas_query = Sintoma.objects.all() #consulta todos los sintomas para agregarlos a una lista
sintomas_choices = []
for s in sintomas_query:
	sintomas_choices.append((s,s))

class FormExpert(forms.Form):
	Seleccione_sintomas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
	 choices=sintomas_choices,)