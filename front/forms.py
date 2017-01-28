from django import forms
from .models import Description, Bill, Sale, Customer

class DForm(forms.ModelForm):
    class Meta:
        db_table = 'inventory'
        model = Description
        fields = ('desc', 'bill', 'length', 'quality', 'rate')

class BForm(forms.ModelForm):
    class Meta:
        db_table = 'inventory_bill'
        model = Bill
        fields = ('party', 'invoice','phone', 'amount', 'bill_name')

class CForm(forms.ModelForm):
    class Meta:
        db_table = 'sale_cust'
        model = Customer
        fields = ('name', 'phone', 'email')

class SForm(forms.ModelForm):
    class Meta:
        db_table = 'sale'
        model = Sale
        fields = ('item_id', 'length', 'cust_id', 'discount', 'tax')
