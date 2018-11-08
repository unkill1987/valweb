from calendar import monthrange


import requests
from django.template import RequestContext
from django.utils.datetime_safe import date
from django.utils.safestring import mark_safe
from pylab import *

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response
import hashlib
import sys
import os
import time

from app.models import Contract, Member, Contract_CI, Contract_SR, Contract_BL, Contract_DO, Contract_LC
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


def share1(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']

    for id in check_ids:
        try:
            share = Contract.objects.get(id=id)
            share.share3=share_user
            share.save()

        except:
            pass
    return redirect('ing')

def share2(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']

    for id in check_ids:
        try:
            share = Contract_CI.objects.get(id=id)
            share.share1=share_user
            share.save()

        except:
            pass
    return redirect('ing2')

def share2_1(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']

    for id in check_ids:
        try:
            share = Contract_SR.objects.get(id=id)
            share.share4=share_user
            share.save()

        except:
            pass
    return redirect('ing2_1')

def share3(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']
    share_user2 = request.GET['share_user2']

    for id in check_ids:
        try:
            share = Contract_LC.objects.get(id=id)
            share.share1=share_user
            share.share2=share_user2
            share.save()

        except:
            pass
    return redirect('ing3')

def share4_1(request):
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']
    share_user2 = request.GET['share_user2']
    for id in check_ids:
        try:
            share = Contract_BL.objects.get(id=id)
            share.share1=share_user
            share.share2=share_user2
            share.save()

        except:
            pass
    return redirect('ing4_1')

def share4_2(request):

    check_id = request.GET['check_id']
    check_ids = check_id.split(',')
    share_user = request.GET['share_user']

    for id in check_ids:
        try:
            share = Contract_DO.objects.get(id=id)
            share.share1=share_user
            share.save()

        except:
            pass
    return redirect('ing4_2')


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
            Contract_CI.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing2')

def remove3(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract_LC.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing3')

def remove2_1(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract_SR.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing2_1')

def remove4_1(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract_BL.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing4_1')

def remove4_2(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            Contract_DO.objects.get(id=id).delete()
        except:
            pass

    return redirect('ing4_2')


def ciremove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_CI.objects.get(id=id)
            share.share1 = ' '
            share.save()
        except:
            pass
    return redirect('cirecieved')


def blremove1(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_BL.objects.get(id=id)
            share.share1 = ' '
            share.save()
        except:
            pass
    return redirect('blrecieved1')

def lcremove1(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_LC.objects.get(id=id)
            share.share1 = ' '
            share.save()
        except:
            pass
    return redirect('lcrecieved1')

def blremove2(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_BL.objects.get(id=id)
            share.share2 = ' '
            share.save()
        except:
            pass
    return redirect('blrecieved2')


def lcremove2(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_LC.objects.get(id=id)
            share.share2 = ' '
            share.save()
        except:
            pass
    return redirect('lcrecieved2')

def doremove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_DO.objects.get(id=id)
            share.share2 = ' '
            share.save()
        except:
            pass
    return redirect('dorecieved')

def lcrremove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract.objects.get(id=id)
            share.share3 = ' '
            share.save()
        except:
            pass
    return redirect('lcrrecieved')


def srremove(request):
    # deletes all objects from Car database table
    # Contract.objects.get('id').delete()
    check_id = request.GET['check_id']
    check_ids = check_id.split(',')

    for id in check_ids:
        try:
            share = Contract_SR.objects.get(id=id)
            share.share4 = ' '
            share.save()
        except:
            pass
    return redirect('cirecieved')

def submit(request):
    contractname = request.POST['contractname']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']
    h = request.POST['h']
    i = request.POST['i']
    j = request.POST['j']
    k = request.POST['k']
    l = request.POST['l']
    m = request.POST['m']
    n = request.POST['n']
    o = request.POST['o']

    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('LCR_' + time_format + '.txt', 'wt')
    file.write('Letter of Credit' + '\n'
'1.Advising bank:' + a + '\n'
'2.Credit No.:' + b + '\n'
'3.Beneficiary:' + c + '\n'
'4.Applicant:' + d + '\n'
'5.L/C Amount and Tolerance:' + e + '\n'
'6.Type:' + f + '\n'
'7.Partial shipment:' + g + '\n'
'8.Transshipment:' + h + '\n'
'9.Trnasport mode:' + i + '\n'
'10.Loading(shipment from):' + j + '\n'
'11.Discharging(shipment to):' + k + '\n'
'12.Latest shipment date:' + l + '\n'
'13.All banking charges:' + m + '\n'
'14.Confirmation:' + n + '\n'
'15.T/T reimbursement:' + o + '\n')
    file.close()

    file = open('LCR_' + time_format + '.txt', 'rb')
    data = file.read()

    # hasher = hashlib.md5()
    # with open('myfile.jpg', 'rb') as afile:
    #     buf = afile.read()
    #     hasher.update(buf)
    # print(hasher.hexdigest())

    # a = 'MD5 : ' + hashlib.md5(data).hexdigest()
    # b = 'SHA-1 : ' + hashlib.sha1(data).hexdigest()
    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract(contractname=contractname, sha256=hash, filename='LCR_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing')

#

def submit2(request):
    invoicename = request.POST['invoicename']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']
    h = request.POST['h']
    i = request.POST['i']
    j = request.POST['j']
    k = request.POST['k']
    l = request.POST['l']
    m = request.POST['m']
    n = request.POST['n']
    o = request.POST['o']
    p = request.POST['p']
    q = request.POST['q']
    r = request.POST['r']



    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('CI_' + time_format + '.txt', 'wt')
    file.write('COMMECIAL INVOICE' + '\n'
                'Invoice name:' + invoicename + '\n'
'1.Shipper/Seller:' + a + '\n'
'2.Consignee:' + b + '\n'
'3.Departure date:' + c + '\n'
'4.Vessel/Flight:' + d + '\n'
'5.From:' + e + '\n'
'6.To:' + f + '\n'
'7.Invoice No.and Date:' + g + '\n'
'8.L/C No.and Date:' + h + '\n'
'9.Buyer(if other than consignee):' + i + '\n'
'10.Other reference:' + j + '\n'
'11.Terms of delivery and payment:' + k + '\n'
'12.Shipping Mark:' + l + '\n'
'13.No.and kind of packages:' + m + '\n'
'14.Goods description:' + n + '\n'
'15.Quantity:' + o + '\n'
'16.Unit price:' + p + '\n'
'17. Amount:' + q + '\n'
'18.Singed by:' + r + '\n'
               )

    file.close()

    file = open('CI_' + time_format + '.txt', 'rb')
    data = file.read()

    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract_CI(contractname=invoicename, sha256=hash, filename='CI_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing2')


def submit2_1(request):
    srname = request.POST['srequestname']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']
    h = request.POST['h']
    i = request.POST['i']
    j = request.POST['j']
    k = request.POST['k']
    l = request.POST['l']
    m = request.POST['m']
    n = request.POST['n']
    o = request.POST['o']




    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('SR_' + time_format + '.txt', 'wt')
    file.write('SHIPPING REQUEST' + '\n'
                'Request name:' + srname + '\n'
'1.Shipper:' + a + '\n'
'2.Consignee:' + b + '\n'
'3.Notify Party:' + c + '\n'
'4.Vessel:' + d + '\n'
'5.Voyage No.:' + e + '\n'
'6.Port of Loading:' + f + '\n'
'7.Port of Discharge:' + g + '\n'
'8.Final Destination:' + h + '\n'
'9.Marking:' + i + '\n'
'10.Packages:' + j + '\n'
'11.Description of Goods:' + k + '\n'
'12.Gross Weight:' + l + '\n'
'13.Measurement:' + m + '\n'
'14.Freight Term:' + n + '\n'
'15.Original B/L:' + o + '\n'

               )

    file.close()

    file = open('SR_' + time_format + '.txt', 'rb')
    data = file.read()

    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract_SR(contractname=srname, sha256=hash, filename='SR_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing2_1')


def submit3(request):
    letteroflc = request.POST['letteroflc']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']
    h = request.POST['h']
    i = request.POST['i']
    j = request.POST['j']
    k = request.POST['k']
    l = request.POST['l']
    m = request.POST['m']
    n = request.POST['n']
    o = request.POST['o']
    p = request.POST['p']
    q = request.POST['q']
    r = request.POST['r']
    s = request.POST['s']
    t = request.POST['t']
    u = request.POST['u']
    v = request.POST['v']
    w = request.POST['w']
    x = request.POST['x']
    y = request.POST['y']
    z = request.POST['z']
    aa = request.POST['aa']
    bb = request.POST['bb']
    cc = request.POST['cc']
    dd = request.POST['dd']
    ee = request.POST['ee']
    ff = request.POST['ff']
    gg = request.POST['gg']

    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('LC_' + time_format + '.txt', 'wt')
    file.write('Letter of Credit' + '\n'
'(APPLICATION FOR IRREVOCABLE DOCUMENTARY CREDIT)' +'\n'+
letteroflc + '\n'
'1.Transfer:' + a + '\n'
'2.Credit Number: ' + b + '\n'
'3.Advising Bank:' + c + '\n'
'4.Expiry Date:' + d + '\n'
'5.Applicant:' + e + '\n'
'6.Beneficiary:' + f + '\n'
'7.Amount:' + g + '\n'
'8.Partial Shipment:' + h + '\n'
'9.Latest Shipment Date:' + i + '\n'
'10.Additional Conditions:' + j + '\n'
'11.All banking charges:' + k + '\n'
'12.Documents delivered by:' + l + '\n'
'13.Confirmation:' + m + '\n'
'14.Reissue:' + n + '\n'
'15.Import L/C Transfer:' + o + '\n'
'16.Draft at:' + p + '\n'
'17.Usance:' + q + '\n'
'18.SettlingBank:' + r + '\n'
'19.Credit:' + s + '\n'
'20.Transshipment mode:' + t + '\n'
'21.Authorization:' + u + '\n'
'22.Port of Loading/Airport of Departure' + v + '\n'
'23.Place of Taking in Charge:' + w + '\n'
'24.SIgned/Original/Commercial Invoice :' + x + '\n'
'25.FULL SET of B/L:' + y + '\n'
'26.Certificate of Origin in :' + z + '\n'
'27.Certificate of Analysis in :' + aa + '\n'
'28.Other Documents Required:' + bb + '\n'
'29.Description of Goods/Services:' + cc + '\n'
'30.Price Terms:' + dd + '\n'
'31.Country of Origin:' + ee + '\n'
'32.HS CODE:' + ff + '\n'
'33.CommodityDescription:' + gg + '\n'

               )

    file.close()

    file = open('LC_' + time_format + '.txt', 'rb')
    data = file.read()

    # hasher = hashlib.md5()
    # with open('myfile.jpg', 'rb') as afile:
    #     buf = afile.read()
    #     hasher.update(buf)
    # print(hasher.hexdigest())
    #
    # a = 'MD5 : ' + hashlib.md5(data).hexdigest()
    # b = 'SHA-1 : ' + hashlib.sha1(data).hexdigest()
    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract_LC(contractname=letteroflc, sha256=hash, filename='LC_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing3')


def submit4_1(request):
    contractname = request.POST['contractname']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']
    h = request.POST['h']
    i = request.POST['i']
    j = request.POST['j']




    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('BL_' + time_format + '.txt', 'wt')
    file.write('BILL OF LADING' + '\n'
                'B/L:' + contractname + '\n'
'1.Bank:' + a + '\n'
'2.Nodify party:' + b + '\n'
'3.Lessel:' + c + '\n'
'4.Voyage No.:' + d + '\n'
'5.Part of loading:' + e + '\n'
'6.Place of receipt:' + f + '\n'
'7.Place of delivery:' + g + '\n'
'8.Description of goods:' + h + '\n'
'9.Weight:' + i + '\n'
'10.Measurement:' + j + '\n'

               )

    file.close()

    file = open('BL_' + time_format + '.txt', 'rb')
    data = file.read()

    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract_BL(contractname=contractname, sha256=hash, filename='BL_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing4_1')


def submit4_2(request):
    contractname = request.POST['contractname']
    a = request.POST['a']
    b = request.POST['b']
    c = request.POST['c']
    d = request.POST['d']
    e = request.POST['e']
    f = request.POST['f']
    g = request.POST['g']





    time_format = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

    file = open('DO_' + time_format + '.txt', 'wt')
    file.write('DO' + '\n'
                'B/L:' + contractname + '\n'
'1.Agent name:' + a + '\n'
'2.Restricted delivery(Yes or no):' + b + '\n'
'3.Adult signature restriced delivery(Yes or no):' + c + '\n'
'4.Agent Signture:' + d + '\n'
'5.ID verified (yes or no):' + e + '\n'
'6.USPS initals:' + f + '\n'
'7.Date:' + g + '\n'


               )

    file.close()

    file = open('DO_' + time_format + '.txt', 'rb')
    data = file.read()

    hash = 'SHA-256 : ' + hashlib.sha256(data).hexdigest()
    file.close()

    # 데이터 저장
    contract = Contract_DO(contractname=contractname, sha256=hash, filename='DO_' + time_format + '.txt')

    # 로그인한 사용자 정보를 Contract에 같이 저장
    user_id = request.session['user_id']
    member = Member.objects.get(user_id=user_id)
    contract.owner = member

    contract.save()

    return redirect('ing4_2')

def download(request):
    id = request.GET['id']
    c = Contract.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response

def download2(request):
    id = request.GET['id']
    c = Contract_CI.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response

def download2_1(request):
    id = request.GET['id']
    c = Contract_SR.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response

def download3(request):
    id = request.GET['id']
    c = Contract_LC.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response

def download4_1(request):
    id = request.GET['id']
    c = Contract_BL.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='text/plain')
        response['Content-Disposition'] = 'inline; filename="{}"'.format(filename)
        return response

def download4_2(request):
    id = request.GET['id']
    c = Contract_DO.objects.get(id=id)

    filepath = os.path.join(settings.BASE_DIR, c.filename)
    # filepath = os.path.join('/home/valkyrie1234', c.filename)
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
        contract = Contract_CI.objects.filter(owner=member).order_by('-id')
        n = len(contract)

        # to = Contract_invoice.objects.get(share1=share1)


        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing2.html', {'contract': contracts, 'n': n, })
    except Exception as e:
        print(e)
        return redirect('login')

def ing2_1(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_SR.objects.filter(owner=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing2_1.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def ing3(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_LC.objects.filter(owner=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing3.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def ing4_1(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_BL.objects.filter(owner=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing4_1.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def ing4_2(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_DO.objects.filter(owner=member).order_by('-id')

        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/ing4_2.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def cirecieved(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_CI.objects.filter(share1=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/cirecieved.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')


def srrecieved(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_SR.objects.filter(share4=member).order_by('-id')

        n = len(contract)
        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/srrecieved.html', {'contract': contracts, 'n': n})
    except Exception as e:
        print(e)
        return redirect('login')


def blrecieved1(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_BL.objects.filter(share1=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/blrecieved1.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def lcrecieved1(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_LC.objects.filter(share1=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/lcrecieved1.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def blrecieved2(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_BL.objects.filter(share2=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/blrecieved2.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def lcrecieved2(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_LC.objects.filter(share2=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/lcrecieved2.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def dorecieved(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract_DO.objects.filter(share2=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/dorecieved.html', {'contract': contracts, 'n': n})
    except:
        return redirect('login')

def lcrrecieved(request):
    try:
        user_id = request.session['user_id']
        member = Member.objects.get(user_id=user_id)
        contract = Contract.objects.filter(share3=member).order_by('-id')
        n = len(contract)

        paginator = Paginator(contract, 6)

        page = request.GET.get('page')
        contracts = paginator.get_page(page)

        return render(request, 'app/lcrrecieved.html', {'contract': contracts, 'n': n})
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
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # res1 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD', headers=headers)
    # json_data = res1.json()
    # basePrice1 = json_data[0]['basePrice']
    # sellprice1 = json_data[0]['cashSellingPrice']
    # buyprice1 = json_data[0]['cashBuyingPrice']
    #
    # res2 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWJPY', headers=headers)
    # json_data = res2.json()
    # basePrice2 = json_data[0]['basePrice']
    # sellprice2 = json_data[0]['cashSellingPrice']
    # buyprice2 = json_data[0]['cashBuyingPrice']
    #
    # res3 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWCNY', headers=headers)
    # json_data = res3.json()
    # basePrice3 = json_data[0]['basePrice']
    # sellprice3 = json_data[0]['cashSellingPrice']
    # buyprice3 = json_data[0]['cashBuyingPrice']

    try:


        user_id = request.session['user_id']
        user_role = request.session['user_role']
        n = len(Contract.objects.filter(owner=Member.objects.get(user_id=user_id)))
        n1 = len(Contract.objects.filter(share1=Member.objects.get(user_id=user_id)))

        templates = ''
        if user_role == '1':
            templates = 'app/index.html'
        elif user_role == '2':
            templates = 'app/index2.html'
        elif user_role == '3':
            templates = 'app/index3.html'
        elif user_role == '4':
            templates = 'app/index4.html'
        else:
            templates = 'app/login.html'

        # return render(request, templates, {'n': n,'n1':n1,'basePrice1': basePrice1,'sellprice1':sellprice1,'buyprice1':buyprice1,
        #                                        'basePrice2':basePrice2,'sellprice2':sellprice2,'buyprice2':buyprice2,
        #                                        'basePrice3':basePrice3,'sellprice3':sellprice3,'buyprice3':buyprice3})
        return render(request, templates,
                      {'n': n, 'n1': n1})

    except Exception as e:
        print(e)
        return redirect('login')


def charts(request):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    # res1 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWUSD', headers=headers)
    # json_data = res1.json()
    # basePrice1 = json_data[0]['basePrice']
    # sellprice1 = json_data[0]['cashSellingPrice']
    # buyprice1 = json_data[0]['cashBuyingPrice']
    #
    # res2 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWJPY', headers=headers)
    # json_data = res2.json()
    # basePrice2 = json_data[0]['basePrice']
    # sellprice2 = json_data[0]['cashSellingPrice']
    # buyprice2 = json_data[0]['cashBuyingPrice']
    #
    # res3 = requests.get('https://quotation-api-cdn.dunamu.com/v1/forex/recent?codes=FRX.KRWCNY', headers=headers)
    # json_data = res3.json()
    # basePrice3 = json_data[0]['basePrice']
    # sellprice3 = json_data[0]['cashSellingPrice']
    # buyprice3 = json_data[0]['cashBuyingPrice']
    # start = datetime.datetime(2018, 10, 1)
    # end = datetime.datetime.now()

    try:

        user_role = request.session['user_role']


        templates = ''
        if user_role == '1':
            templates = 'app/charts.html'
        elif user_role == '2':
            templates = 'app/charts2.html'
        elif user_role == '3':
            templates = 'app/charts3.html'
        elif user_role == '4':
            templates = 'app/charts4.html'
        else:
            templates = 'app/login.html'

        # return render(request, templates, {'basePrice1': basePrice1,'sellprice1':sellprice1,'buyprice1':buyprice1,
        #                                    'basePrice2':basePrice2,'sellprice2':sellprice2,'buyprice2':buyprice2,
        #                                    'basePrice3':basePrice3,'sellprice3':sellprice3,'buyprice3':buyprice3})
        return render(request, templates, {})
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
            templates = 'app/calendar3.html'
        elif user_role == '4':
            templates = 'app/calendar4.html'
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

def forms2(request):
    return render(request, 'app/forms2.html', {})

def forms2_1(request):
    return render(request, 'app/forms2_1.html', {})

def forms3(request):
    return render(request, 'app/forms3.html', {})

def forms4_1(request):
    return render(request, 'app/forms4_1.html', {})

def forms4_2(request):
    return render(request, 'app/forms4_2.html', {})

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
