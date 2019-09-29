from django.shortcuts import render, reverse, HttpResponse
from django_downloadview import ObjectDownloadView
from .models import CV


class Download(ObjectDownloadView):

    def counter(self, pk):
        cv = CV.objects.get(pk=pk)
        cv.download_count += 1
        cv.save()

    def get(self, request, pk):
        self.counter(pk)
        client_ip = request.META['REMOTE_ADDR']
        print(client_ip)

        return super(Download, self).get(request)

