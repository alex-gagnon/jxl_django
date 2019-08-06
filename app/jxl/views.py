from django.shortcuts import render
from django.views.generic import FormView

from .forms import JXLForm


class HomeView(FormView):
    template_name = 'jxl/home.html'
    form_class = JXLForm

    def form_valid(self, form):
        return super().form_valid(form)


def home_page(request):
    form = {'form': JXLForm, 'title': 'Home', 'submit_btn': 'Download Report'}
    return render(request, 'jxl/home.html', form)
