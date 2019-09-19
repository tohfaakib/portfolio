from django.urls import path
from django_downloadview import ObjectDownloadView
from .models import CV

# ObjectDownloadView inherits from django.views.generic.BaseDetailView.
download = ObjectDownloadView.as_view(model=CV, file_field='file')

urlpatterns = [
    path('download/<int:pk>', download, name='download_cv'),
]
