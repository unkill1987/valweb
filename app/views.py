from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html',{})

def charts(request):
    return render(request, 'app/charts.html',{})