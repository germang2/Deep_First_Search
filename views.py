from django.shortcuts import render, render_to_response
from form import tesoro
from dfs import main

def home(request):
	form = tesoro(request.POST or None)
	text = ""
	if form.is_valid():
		data = form.cleaned_data
		t = data.get('Tesoro')
		#print t
		text = main(t)
		#print text
	context = {
		'form':form,
		'text':text
	}
	return render(request,"inicio.html",context)