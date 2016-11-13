from django import forms

sintomas_choices = (
	('Tos', 'Tos'),
	('Opresion muscular', 'Opresion muscular'),
	('Nauseas', 'Nauseas'),
	('Molestia en el pecho', 'Molestia en el pecho'),
	('Fiebre', 'Fiebre'),
	('Fatiga', 'Fatiga'),
	('Escalofrios', 'Escalofrios'),
	('Dolor en el pecho', 'Dolor en el pecho'),
	('Dolor de garganta', 'Dolor de garganta'),
	('Dolor de cabeza', 'Dolor de cabeza'),
	('Dificultad respiratoria', 'Dificultad respiratoria'),
	('Congestion nasal', 'Congestion nasal'),
)

class FormExpert(forms.Form):
	Seleccione_sintomas = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
	 choices=sintomas_choices,)