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
    price=items[0].find(class_='style__price-tag___B2csA').get_text()
    quantity=items[0].find(class_='style__pack-size___254Cd').get_text()
    med_name=items[0].find(class_='style__pro-title___3zxNC').get_text()
    img_div=items[0].find(class_='')
    img1=img_div.find('img')
    img_src=img1['src']
    # print(img_div)
    # print(med_name)

    context={
             'img_src' : img_src,
             'med_name': med_name,
             'price' : price,
             'quantity' : quantity
       }
    return render(request,'send/medical.html',context)

def login(request):
    return HttpResponse("login")

def validate(request):
    return render(request,'send/validate.html')