from django.shortcuts import render, render_to_response
from form import tesoro
from dfs import main

def home(request):
	text = ""
	t = ''
	if request.POST:
		#form = tesoro(request.POST)
		#if form.is_valid():
			#data = form.cleaned_data
			#print t
		data = main()
		text = data[0]
		t = data[1]
	else:
		#form = tesoro()
		text = ""

	context = {}	
	context = {
		#'form':form,
		'text':text,
		't': t,
	}
	return render(request,"inicio.html",context)