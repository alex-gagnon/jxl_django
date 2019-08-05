from django.shortcuts import render

from jxl.forms import JXLForm


def home_page(request):
    form = {'form': JXLForm, 'title': 'Home', 'submit_btn': 'Download Report'}
    return render(request, 'home.html', form)
