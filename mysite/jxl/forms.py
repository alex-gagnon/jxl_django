from django import forms
from django.forms import ModelForm

from .models import JXLModel


class JXLForm(ModelForm):
    title = 'Home'
    project = forms.ModelChoiceField(label='Project:',
                                     queryset=JXLModel.objects.distinct('project_text'),
                                     to_field_name='project_code')
    filter_by = forms.ModelChoiceField(label='Filter by:',
                                       queryset=JXLModel.objects.values_list('filter_by_text', flat=True).distinct(),
                                       to_field_name='filter_by_code')
    version = forms.CharField(label='Version:',
                              min_length=2,
                              max_length=40,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Enter version number (e.g. 10.2)'}))

    class Meta:
        model = JXLModel
        fields = ['project_text', 'filter_by_text']

    def __init__(self, *args, **kwargs):
        super(JXLForm, self).__init__(*args, **kwargs)
