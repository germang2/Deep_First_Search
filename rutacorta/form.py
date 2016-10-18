from django import forms

class RutaCorta(forms.Form):
	Ciudad_inicio = forms.CharField(max_length=1)
	Ciudad_destino = forms.CharField(max_length=1)