from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'home.html')

def send_email(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)

        send_mail(
            # name,
            subject,
            message,
            'graphicx.mehfooz201@gmail.com',
            ['graphicx.mehfooz201@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect('/')
    else:
        return HttpResponse('Invalid Request ! ')