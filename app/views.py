import mpld3
import requests
from pylab import *
import pandas_datareader.data as web
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import hashlib
import sys
import os
import time
from app.models import Contract, Member
from valweb import settings
from django.utils import timezone


def paging(request):
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract_list = Contract.objects.filter(owner=member)
    paginator = Paginator(contract_list, 6)

    page = request.GET.get('page')
    contracts = paginator.get_page(page)
    return render(request, 'app/ing.html', {'contracts': contracts})


def share(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']

    for id in check_ids:
        try:
            share = Contract.objects.get(id=id)
            share.share1=share_user
            share.save()

        except:
            pass
    return redirect('ing')




def remove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing')

def remove2(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            remove = Contract.objects.get(id=id)
            remove.share1 = ' '
            remove.save()
        except:
            pass

    return redirect('ing2')


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

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing')
    # return render(request, 'app/submit.html', {'contractname': contractname, 'a': a, 'b': b, 'c': c})
#

def download(request):
    id = request.GET['id']
    c = Contract.objects.get(id=id)

    # filepath = os.path.join(settings.BASE_DIR, c.filename)
    filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response


def ing(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract.objects.filter(owner=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def ing2(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract.objects.filter(share1=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing2.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')


def done(request):

    try:
        user_role = request.session['user_role']

        templates = ''
        if user_role == '1':
            templates = 'app/done.html'
        elif user_role == '2':
            templates = 'app/done2.html'
        elif user_role == '3':
            templates = 'app/blank.html'
        elif user_role == '4':
            templates = 'app/blank.html'
        else:
            templates = 'app/login.html'
        return render(request, templates, {})
    except:
        return redirect('login')


def logout(request):
    try:
        del request.session['user_role']
        del request.session['user_id']
        return redirect('login')
    except:
        return render(request, 'app/login.html',{})



def index(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res1 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD', headers=headers)
    json_data = res1.json()
    basePrice1 = json_data[0]['basePrice']
    sellprice1 = json_data[0]['cashSellingPrice']
    buyprice1 = json_data[0]['cashBuyingPrice']

    res2 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWJPY', headers=headers)
    json_data = res2.json()
    basePrice2 = json_data[0]['basePrice']
    sellprice2 = json_data[0]['cashSellingPrice']
    buyprice2 = json_data[0]['cashBuyingPrice']

    res3 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWCNY', headers=headers)
    json_data = res3.json()
    basePrice3 = json_data[0]['basePrice']
    sellprice3 = json_data[0]['cashSellingPrice']
    buyprice3 = json_data[0]['cashBuyingPrice']

    try:


        user_id = request.session['user_id']
        user_role = request.session['user_role']
        n = len(Contract.objects.filter(owner=Member.objects.get(user_id=user_id)))

        templates = ''
        if user_role == '1':
            templates = 'app/index.html'
        elif user_role == '2':
            templates = 'app/index2.html'
        elif user_role == '3':
            templates = 'app/blank.html'
        elif user_role == '4':
            templates = 'app/blank.html'
        else:
            templates = 'app/login.html'

        return render(request, templates, {'n': n,'basePrice1': basePrice1,'sellprice1':sellprice1,'buyprice1':buyprice1,
                                               'basePrice2':basePrice2,'sellprice2':sellprice2,'buyprice2':buyprice2,
                                               'basePrice3':basePrice3,'sellprice3':sellprice3,'buyprice3':buyprice3})
    except:
        return redirect('login')


def charts(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    res1 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD', headers=headers)
    json_data = res1.json()
    basePrice1 = json_data[0]['basePrice']
    sellprice1 = json_data[0]['cashSellingPrice']
    buyprice1 = json_data[0]['cashBuyingPrice']

    res2 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWJPY', headers=headers)
    json_data = res2.json()
    basePrice2 = json_data[0]['basePrice']
    sellprice2 = json_data[0]['cashSellingPrice']
    buyprice2 = json_data[0]['cashBuyingPrice']

    res3 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWCNY', headers=headers)
    json_data = res3.json()
    basePrice3 = json_data[0]['basePrice']
    sellprice3 = json_data[0]['cashSellingPrice']
    buyprice3 = json_data[0]['cashBuyingPrice']
    start = datetime.datetime(2018, 10, 1)
    end = datetime.datetime.now()

    try:

        user_role = request.session['user_role']


        templates = ''
        if user_role == '1':
            templates = 'app/charts.html'
        elif user_role == '2':
            templates = 'app/charts2.html'
        elif user_role == '3':
            templates = 'app/blank.html'
        elif user_role == '4':
            templates = 'app/blank.html'
        else:
            templates = 'app/login.html'

        return render(request, templates, {'basePrice1': basePrice1,'sellprice1':sellprice1,'buyprice1':buyprice1,
                                           'basePrice2':basePrice2,'sellprice2':sellprice2,'buyprice2':buyprice2,
                                           'basePrice3':basePrice3,'sellprice3':sellprice3,'buyprice3':buyprice3})
    except:
        return redirect('login')





def calendar(request):
    try:
        user_role = request.session['user_role']

        templates = ''
        if user_role == '1':
            templates = 'app/calendar.html'
        elif user_role == '2':
            templates = 'app/calendar2.html'
        elif user_role == '3':
            templates = 'app/blank.html'
        elif user_role == '4':
            templates = 'app/blank.html'
        else:
            templates = 'app/login.html'

        return render(request, templates, {})
    except:
        return redirect('login')



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
        email = request.POST['email']
        password = request.POST['password']
        user_role = request.POST['user_role']

        result_dict = {}
        try:
            Member.objects.get(user_role=user_role, user_id=email, user_pw=password)
            result_dict['result'] = 'success'
            request.session['user_id'] = email
            request.session['user_role'] = user_role
        except Member.DoesNotExist:
            result_dict['result'] = 'fail'
        return JsonResponse(result_dict)




def register(request):
    if request.method == 'GET':
        return render(request, 'app/register.html', {})
    else:
        result_dict = {}
        try:
            user_role = request.POST['user_role']
        except:
            user_role = ''

        user_name = request.POST['user_name']
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_confirm_pw = request.POST['user_confirm_pw']

        if user_role == '' or user_name == '' or user_id == '' or user_pw == '' or user_confirm_pw == '':
            result_dict['result'] = '공백은 사용할 수 없습니다.'
            return JsonResponse(result_dict)

        elif user_pw != user_confirm_pw:
            result_dict['result'] = '비밀번호 매치 실패'
            return JsonResponse(result_dict)

        else:
            try:
                Member.objects.get(user_id=user_id)
                result_dict['result'] = '이미 가입된 아이디가 있습니다.'
            except Member.DoesNotExist:
                member = Member(user_role=user_role, user_id=user_id, user_pw=user_pw, user_name=user_name)
                member.c_date = timezone.now()
                member.save()
                result_dict['result'] = '가입완료'

            return JsonResponse(result_dict)


def forgot(request):
    return render(request, 'app/forgot.html', {})
