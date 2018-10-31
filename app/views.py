from django.http import HttpResponse
from django.shortcuts import render
import hashlib
import sys
import os


import time
# Create your views here.
def submit(request):
    cable = request.POST['cable']
    mail = request.POST['mail']
    telex = request.POST['telex']
    to = request.POST['to']
    dear = request.POST['dear']
    applicant = request.POST['applicant']
    beneficiary = request.POST['beneficiary']
    bank = request.POST['bank']
    date = request.POST['date']
    place = request.POST['place']
    code = request.POST['code']
    camount = request.POST['camount']
    cwith = request.POST['with']
    exporter = request.POST['exporter']
    commodity = request.POST['commodity']
    quantity = request.POST['quantity']
    price = request.POST['price']
    amount = request.POST['amount']

    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('계약_' + time_format + '.txt', 'wt')
    file.write('Letter of Credit'+'\n'
                'Address Form'+'\n'
                'Cable Address:' + cable + '\n'
               'Mailing Address:' + mail +'\n'
               'Telex Number:' + telex + '\n'
               'To:' + to +'\n'
               'Dear Sirs:' + dear +'\n'
               'Bank Form'+'\n'
               'Applicant:'+applicant +'\n'
               'Beneficiary:' + beneficiary +'\n'
               'Advising Bank;' + bank +'\n'
               'Expiry Date:' +date+'\n'
               'Expiry Place:'+place+'\n'
               'Currency Code:' +code+'\n'
                'Currency Amount:'+camount+'\n'
               'Credit Available With:'+cwith+'\n'
                'Order Form'+'\n'
               'Exporter:'+exporter +'\n'
               'Name of Commodity:' + commodity +'\n'
               'Quantity:'+quantity+'\n'
               'Unit Price:'+price+'\n'
               'Amount:' +amount+'\n')
    file.close()

    file = open('계약_' + time_format + '.txt', 'rb')
    data = file.read()

    # hasher = hashlib.md5()
    # with open('myfile.jpg', 'rb') as afile:
    #     buf = afile.read()
    #     hasher.update(buf)
    # print(hasher.hexdigest())

    a= 'MD5 : ' + hashlib.md5(data).hexdigest()
    b= 'SHA-1 : ' + hashlib.sha1(data).hexdigest()
    c= 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()


    return render(request, 'app/submit.html',{'a':a,'b':b,'c':c})


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
    if request.method == 'GET':
        return render(request, 'app/register.html', {})
    else:
        user_id = request.POST['user_id']
        user_name = request.POST['user_name']
        print(user_id, user_name)
        return HttpResponse('회원가입 완료')


def forgot(request):
    return render(request, 'app/forgot.html', {})
