from django.shortcuts import render

# Create your views here.
def rutacorta(request):
	return render(request, 'rutacorta.html', {})