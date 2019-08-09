import os

from django.http import HttpResponse, FileResponse
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
        response = HttpResponse(open(file.get('filepath'), 'rb').read())
        response['Content-Type'] = 'mimetype/submimetype'
        response['Content-Disposition'] = f"attachment; filename={file.get('filename')}"
        return response

    def form_invalid(self, form):
        return HttpResponse(f"<p>{form.errors}</h1>")

    @staticmethod
    def send_file( data):
        project = {'project': data.get('project_text'),
                   'filter_by': data.get('filter_by_text'),
                   'version': data.get('version')}
        response = JXL(**auth, **project)
        response.get_filtered_jira_issues()

        return response.download(response.write_data())
