from django import forms

from .choices import projects, filters


class JXLForm(forms.Form):
    title = 'Home'
    project = forms.ChoiceField(label='Project:', choices=projects)
    filter_by = forms.ChoiceField(label='Filter by:', choices=filters)
    version = forms.CharField(label='Version:',
                              min_length=2,
                              max_length=40,
                              widget=forms.TextInput(
                                  attrs={'placeholder': 'Enter version number (e.g. 10.2)'}))
