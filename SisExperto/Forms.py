from django import forms

class FormExpert(forms.Form):
	elecciones = (('y','Si'), ('n','No'))
	campo = forms.ChoiceField(widget=forms.RadioSelect, choices=elecciones)