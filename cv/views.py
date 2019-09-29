from django.shortcuts import render, reverse, HttpResponse
from django_downloadview import ObjectDownloadView
from .models import CV, IP


class Download(ObjectDownloadView):

    def counter(self, request, pk):
        cv = CV.objects.get(pk=pk)
        ip = IP()

        client_ip = request.META['REMOTE_ADDR']
        # print(str(cv.ip.all()))

        if client_ip not in str(cv.ip.all()):
            ip.ip_list = client_ip
            ip.save()

            cv.ip.add(ip)
            cv.unique_download += 1
            cv.total_download += 1
            cv.save()
        else:
            cv.total_download += 1
            cv.save()

    def get(self, request, pk):
        self.counter(request, pk)

        return super(Download, self).get(request)

