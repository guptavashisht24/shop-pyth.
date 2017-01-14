from django import forms

from .models import Description, Bill


class DForm(forms.ModelForm):
    class Meta:
     
        model = Description
        fields = ('desc', 'billing', 'length', 'quality', 'rate')

class BForm(forms.ModelForm):
    party = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Party'}))
    inovice = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Invoice#'}))
    amount = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Bill-Amount'}))
    image = forms.ImageField()
    image_caption = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Description for bill'}))
    class Meta:
        model = Bill
        fields = ('party', 'inovice', 'amount','image','image_caption')
