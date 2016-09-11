from django.shortcuts import render, render_to_response
#from form import tesoro
#from dfs import main

def home(request):
	context = {}
	return render(request,"inicio.html",context)