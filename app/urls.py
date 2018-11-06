"""valweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from app.views import srrecieved

urlpatterns = [

    path('index/',views.index, name='index'),
    path('index2/',views.index, name='index2'),
    path('index3/',views.index, name='index3'),
    path('index4/',views.index, name='index4'),

    path('charts/', views.charts, name='charts'),
    path('charts2/', views.charts, name='charts2'),
    path('charts3/', views.charts, name='charts3'),
    path('charts4/', views.charts, name='charts4'),

    path('ing/', views.ing, name='ing'),
    path('ing2/', views.ing2, name='ing2'),
    path('ing2_1/', views.ing2_1, name='ing2_1'),
    path('ing3/', views.ing3, name='ing3'),
    path('ing4_1/', views.ing4_1, name='ing4_1'),
    path('ing4_2/', views.ing4_2, name='ing4_2'),

    path('calendar/', views.calendar, name='calendar'),
    path('calendar2/', views.calendar, name='calendar2'),
    path('calendar3/', views.calendar, name='calendar3'),
    path('calendar4/', views.calendar, name='calendar4'),

    path('done/', views.done, name='done'),
    path('done2/', views.done, name='done2'),

    path('remove/', views.remove, name='remove'),
    path('remove2/', views.remove2, name='remove2'),
    path('remove2_1/', views.remove2_1, name='remove2_1'),
    path('remove3/', views.remove3, name='remove3'),
    path('remove4_1/', views.remove4_1, name='remove4_1'),
    path('remove4_2/', views.remove4_2, name='remove4_2'),

    path('shareremove1/', views.shareremove1, name='shareremove1'),
    path('shareremove2/', views.shareremove2, name='shareremove2'),
    path('shareremove2_1/', views.shareremove2_1, name='shareremove2_1'),
    path('shareremove4_1/', views.shareremove4_1, name='shareremove4_1'),

    path('forms/', views.forms, name='forms'),
    path('forms2/', views.forms2, name='forms2'),
    path('forms2_1/', views.forms2_1, name='forms2_1'),
    path('forms3/', views.forms3, name='forms3'),
    path('forms4_1/', views.forms4_1, name='forms4_1'),
    path('forms4_2/', views.forms4_2, name='forms4_2'),

    path('submit/', views.submit, name='submit'),
    path('submit2/', views.submit2, name='submit2'),
    path('submit2_1/', views.submit2_1, name='submit2_1'),
    path('submit3/', views.submit3, name='submit3'),
    path('submit4_1/', views.submit4_1, name='submit4_1'),
    path('submit4_2/', views.submit4_2, name='submit4_2'),

    path('share1/', views.share1, name='share1'),
    path('share2/', views.share2, name='share2'),
    path('share2_1/', views.share2_1, name='share2_1'),
    path('share3/', views.share3, name='share3'),
    path('share4_1/', views.share4_1, name='share4_1'),
    path('share4_2/', views.share4_2, name='share4_2'),


    path('cirecieved/', views.cirecieved, name='cirecieved'),
    path('blrecieved1/', views.blrecieved1, name='blrecieved1'),
    path('blrecieved2/', views.blrecieved2, name='blrecieved2'),
    path('dorecieved/', views.dorecieved, name='dorecieved'),
    path('srrecieved', views.srrecieved, name='srrecieved'),
    path('lcrecieved1/', views.lcrecieved1, name='lcrecieved1'),
    path('lcrecieved2/', views.lcrecieved2, name='lcrecieved2'),
    path('lcrrecieved/', views.lcrrecieved, name='lcrrecieved'),


    path('blremove1/', views.blremove1, name='blremove1'),
    path('blremove2/', views.blremove2, name='blremove2'),
    path('lcremove1/', views.lcremove1, name='lcremove1'),
    path('lcremove2/', views.lcremove2, name='lcremove2'),
    path('doremove/', views.doremove, name='doremove'),
    path('lcrremove/', views.lcrremove, name='lcrremove'),

    path('download/', views.download, name='download'),
    path('download2/', views.download2, name='download2'),
    path('download2_1/', views.download2_1, name='download2_1'),
    path('download3/', views.download3, name='download3'),
    path('download4_1/', views.download4_1, name='download4_1'),
    path('download4_2/', views.download4_1, name='download4_2'),


    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('logout/', views.logout, name='logout'),
    path('money/', views.money, name='money'),
    path('people/', views.people, name='people'),

]
