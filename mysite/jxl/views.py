import logging
import os

import boto3
from botocore.exceptions import ClientError
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from . import auth
from .forms import JXLForm
from .services import JXL


class HomeView(FormView):
    template_name = 'jxl/home.html'
    form_class = JXLForm
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        file = self.send_file(form.data)
        file_location = file.get('filepath')
        r = self.upload_file(file_name=file_location,
                             object_name=os.path.join(settings.MEDIAFILES_LOCATION, 'jxl', file.get('filename')))

        response = HttpResponse(open(file.get('filepath'), 'rb').read())
        response['Content-Type'] = 'mimetype/submimetype'
        response['Content-Disposition'] = f"attachment; filename={file.get('filename')}"
        return response

    def form_invalid(self, form):
        return HttpResponse(f"<p>{form.errors}</h1>")

    @staticmethod
    def upload_file(file_name, object_name=None):
        """Upload a file to an S3 bucket"""

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        s3_bucket = settings.AWS_STORAGE_BUCKET_NAME
        try:
            response = s3_client.upload_file(file_name, s3_bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    @staticmethod
    def download_file():
        pass

    @staticmethod
    def send_file(data):
        project = {'project': data.get('project_text'),
                   'filter_by': data.get('filter_by_text'),
                   'version': data.get('version')}
        response = JXL(**auth, **project)
        response.get_filtered_jira_issues()

        return response.download(response.write_data())
