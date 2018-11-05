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

urlpatterns = [

    path('index/',views.index, name='index'),
    path('index2/',views.index, name='index2'),

    path('charts/', views.charts, name='charts'),
    path('charts2/', views.charts, name='charts2'),

    path('ing/', views.ing, name='ing'),
    path('ing2/', views.ing2, name='ing2'),

    path('calendar/', views.calendar, name='calendar'),
    path('calendar2/', views.calendar, name='calendar2'),

    path('done/', views.done, name='done'),
    path('done2/', views.done, name='done2'),

    path('remove/', views.remove, name='remove'),
    path('remove2/', views.remove2, name='remove2'),

    path('forms/', views.forms, name='forms'),
    path('forms2/', views.forms2, name='forms2'),

    path('money/', views.money, name='money'),
    path('people/', views.people, name='people'),

    path('submit/', views.submit, name='submit'),
    path('submit2/', views.submit2, name='submit2'),

    path('share1/', views.share1, name='share1'),
    path('share2/', views.share2, name='share2'),

    path('shared/', views.shared, name='shared'),
    path('shared2/', views.shared2, name='shared2'),

    path('submit/', views.submit, name='submit'),
    path('submit2/', views.submit2, name='submit2'),



    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('forgot/', views.forgot, name='forgot'),
    path('download/', views.download, name='download'),
    path('logout/', views.logout, name='logout'),

]
