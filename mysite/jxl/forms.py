from django import forms
from django.forms import ModelForm

from .models import Filter, Project


class JXLForm(ModelForm):
    title = 'Home'
    project_text = forms.ModelChoiceField(label='Project:',
                                          queryset=Project.objects.only('project_text'),
                                          to_field_name='project_code')
    filter_by_text = forms.ModelChoiceField(label='Filter by:',
                                            queryset=Filter.objects.only('filter_by_text'),
                                            to_field_name='filter_by_code')
    version = forms.CharField(label='Version:',
                              min_length=2,
                              max_length=40,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Enter version number (e.g. 10.2)'}))

    class Meta:
        model = Filter
        fields = ['project_text', 'filter_by_text']

    def __init__(self, *args, **kwargs):
        super(JXLForm, self).__init__(*args, **kwargs)
