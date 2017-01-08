from django import forms

from .models import Description

class DForm(forms.ModelForm):

    class Meta:
        model = Description
        fields = ('desc','bill','length','quality','rate')
