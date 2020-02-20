from django.shortcuts import render

from django.http import HttpResponse

from django.core.mail import send_mail

import requests 

from bs4 import BeautifulSoup

import pandas as pd

def index(request):
     email = request.POST['email_id']
     send_mail(
        'Automated mail',
        'automatic mail',
        'starwargamer532@gmail.com',
        [email],
        fail_silently=False,)
     return render(request,'send/index.html')
# Create your views here.

def medic_search(request):
    search=request.POST.get('search')
    web_link='https://www.1mg.com/search/all?name='+search
    page=requests.get(web_link)
    soup=BeautifulSoup(page.content,'html.parser')
    items=soup.find_all(class_='col-xs-12 col-md-9 col-sm-9 style__container___cTDz0')
    med_name=''
    price=''
    quantity=''
    if not items:
        print('its empty dude')
        items=soup.find_all(class_='col-md-3 col-sm-4 col-xs-6 style__container___jkjS2')
        if items:
            med_name=items[0].find(class_='style__pro-title___3G3rr').get_text()
            price='MRP '
            price+=items[0].find(class_='style__discount-price___qlNIB').get_text()
            quantity=items[0].find(class_='style__pack-size___3jScl').get_text() 
            print(med_name)
            print(price)
            print(quantity)
    else:
        price=items[0].find(class_='style__price-tag___B2csA').get_text()
        quantity=items[0].find(class_='style__pack-size___254Cd').get_text()
        med_name=items[0].find(class_='style__pro-title___3zxNC').get_text()
    if not items:
        items_div=soup.find_all(class_='col-xs-12 style__container___3ZesX')
        if items:
            items=items_div[0].find_all('a')
            med_name=items[0].get_text()
        med_name='sorry, we can\'t currently find the medicine' 
        price=''
        quantity=''
        print(med_name)
    context={
            'med_name': med_name,
            'price' : price,
            'quantity' : quantity,
    }

    return render(request,'send/validate.html',context)

def login(request):
    return HttpResponse("login")

def validate(request):
    return render(request,'send/validate.html')