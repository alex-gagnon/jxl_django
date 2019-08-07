from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import FormView

from .forms import JXLForm


class HomeView(FormView):
    template_name = 'jxl/home.html'
    form_class = JXLForm
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('/')

    def get_queryset(self):
        """Return the last published projects, not including those set to be published in the future."""
        return JXLForm.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

    def form_valid(self, form):
        self.send_file(form.cleaned_data)
        return HttpResponse("<h1>Success</h1>")

    def form_invalid(self, form):
        return HttpResponse(f"<p>{form.errors}</h1>")

    def send_file(self, valid_data):
        print(valid_data)
