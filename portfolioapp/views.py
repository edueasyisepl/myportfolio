from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.contrib import messages
from portfolioapp.models import message

# Create your views here.
def home(request):
    return render(request, 'index.html')

def send_message(request):
    if request.method == 'GET':
        fname = request.GET.get('fname')
        lname = request.GET.get('lname')
        email = request.GET.get('email')
        msg = request.GET.get('msg')
        snd_msg = message.objects.create(First_Name=fname, Last_Name=lname, Email_Address=email, Message=msg)
        snd_msg.save()
        messages.success(request, "Thanks for sending message. We will reply very soon to your idea...")
        return redirect('/')