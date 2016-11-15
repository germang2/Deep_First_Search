from django import forms
from .models import Sintoma
'''
sintomas_query = Sintoma.objects.all() #consulta todos los sintomas para agregarlos a una lista
sintomas_choices = []
for s in sintomas_query:
	sintomas_choices.append((s,s))
'''
sintomas_choices = (
    ('Tos','Tos'),
    ('Fiebre','Fiebre'),
    ('Opresion muscular','Opresion muscular'),
    ('Nauseas','Nauseas'),
    ('Molestia en el pecho', '	Molestia en el pecho'),
    ('Fatiga','Fatiga'),
    ('Escalofrios', 'Escalofrios'),
    ('Dolor en el pecho','Dolor en el pecho'),
    ('Dolor de garganta', 'Dolor de garganta'),
    ('Dolor de cabeza','Dolor de cabeza'),
    ('Dificultad respiratoria','Dificultad respiratoria'),
    ('Congestion nasal','Congestion nasal'),
    )
class FormExpert(forms.Form):
	Seleccione_sintomas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
	 choices=sintomas_choices,)