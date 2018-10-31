from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib
import sys
import os
import time
from app.models import Contract
from valweb import settings


def remove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract.objects.get(id=id).delete()
            return redirect('ing')

        except:
            return redirect('ing')


def submit(request):
    contractname = request.POST['contractname']
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

    file = open('contract_' + time_format + '.txt', 'wt')
    file.write('Letter of Credit' + '\n'
                                    'Contract:' + contractname + '\n'
                                                                 'Address Form' + '\n'
                                                                                  'Cable Address:' + cable + '\n'
                                                                                                             'Mailing Address:' + mail + '\n'
                                                                                                                                         'Telex Number:' + telex + '\n'
                                                                                                                                                                   'To:' + to + '\n'
                                                                                                                                                                                'Dear Sirs:' + dear + '\n'
                                                                                                                                                                                                      'Bank Form' + '\n'
                                                                                                                                                                                                                    'Applicant:' + applicant + '\n'
                                                                                                                                                                                                                                               'Beneficiary:' + beneficiary + '\n'
                                                                                                                                                                                                                                                                              'Advising Bank:' + bank + '\n'
                                                                                                                                                                                                                                                                                                        'Expiry Date:' + date + '\n'
                                                                                                                                                                                                                                                                                                                                'Expiry Place:' + place + '\n'
                                                                                                                                                                                                                                                                                                                                                          'Currency Code:' + code + '\n'
                                                                                                                                                                                                                                                                                                                                                                                    'Currency Amount:' + camount + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                   'Credit Available With:' + cwith + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                      'Order Form' + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                     'Exporter:' + exporter + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              'Name of Commodity:' + commodity + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 'Quantity:' + quantity + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          'Unit Price:' + price + '\n'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  'Amount:' + amount + '\n')
    file.close()

    file = open('contract_' + time_format + '.txt', 'rb')
    data = file.read()

    # hasher = hashlib.md5()
    # with open('myfile.jpg', 'rb') as afile:
    #     buf = afile.read()
    #     hasher.update(buf)
    # print(hasher.hexdigest())

    a = 'MD5 : ' + hashlib.md5(data).hexdigest()
    b = 'SHA-1 : ' + hashlib.sha1(data).hexdigest()
    c = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract(contractname=contractname, md5=a, sha1=b, sha256=c, filename='contract_' + time_format + '.txt')
    contract.save()

    return render(request, 'app/submit.html', {'contractname': contractname, 'a': a, 'b': b, 'c': c})


def download(request):
    id = request.GET['id']
    c = Contract.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response


def ing(request):
    n = Contract.objects.count()
    contract = Contract.objects.order_by('-id')

    return render(request, 'app/ing.html', {'contract': contract, 'n': n})


def done(request):
    return render(request, 'app/done.html', {})


def index(request):
    n = Contract.objects.count()

    return render(request, 'app/index.html', {'n': n})


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
