from django.urls import path, include

from .views import email_sending

urlpatterns = [
    path('email_sending/', email_sending, name='send_mail'),
]