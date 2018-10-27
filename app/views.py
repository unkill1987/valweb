from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'app/index.html', {})


def charts(request):
    return render(request, 'app/charts.html', {})


def calendar(request):
    return render(request, 'app/calendar.html', {})


def money(request):
    return render(request, 'app/money.html', {})


def people(request):
    return render(request, 'app/people.html', {})
