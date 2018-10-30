from django.http import HttpResponse
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

def forms(request):
    return render(request, 'app/forms.html', {})


def login(request):
    if request.method == 'GET':
        return render(request, 'app/login.html', {})
    else:
        return HttpResponse()


def register(request):
    if request.method =='GET':
        return render(request,'app/register.html',{})
    else:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        print(user_id, user_name)
        return HttpResponse('회원가입 완료')
