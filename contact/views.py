from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def email_sending(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        messages = request.POST.get("message")


        subject = email + ': '+subject
        message = messages
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tnishan7@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=True)

        # contacts = Contact()
        #
        # contacts.name = name
        # contacts.email = email
        # contacts.country = country
        # contacts.subject = subject
        # contacts.messages = messages
        #
        # contacts.save()

        context = {
            'msg': 'Message Sent!'
        }
        return redirect('/#contact', context)
    return render(request, 'base.html')
