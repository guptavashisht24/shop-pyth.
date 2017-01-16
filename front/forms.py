from django import forms

from .models import Description, Bill

class DForm(forms.ModelForm):
    class Meta:
        db_table = 'inventory'
        model = Description
        fields = ('desc', 'bill', 'length', 'quality', 'rate')

class BForm(forms.ModelForm):
    class Meta:
        db_table = 'inventory_bill'
        model = Bill
        fields = ('party', 'invoice', 'amount', 'bill_name')
