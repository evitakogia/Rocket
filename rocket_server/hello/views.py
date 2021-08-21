from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {"name": request.GET['name']}
    return render(request, 'hello/index.html', context)
