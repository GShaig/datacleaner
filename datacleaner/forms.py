from django import forms
from .models import DataInput

class DataForm(forms.ModelForm):
    method_choices = [
        ('1', 'Delete'),
        ('0', 'Fill')
    ]
    clean_null = forms.ChoiceField(widget=forms.RadioSelect, choices=method_choices, required=False)
    clean_duplicate = forms.BooleanField(initial=False, required=False)
    class Meta:
        model = DataInput
        fields = ('upload', 'filling')