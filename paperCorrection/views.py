from django.shortcuts import render

from django.http import HttpResponse

from django.core.mail import send_mail

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
def login(request):
    return HttpResponse("login")

def validate(request):
    return render(request,'send/validate.html')