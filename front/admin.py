from django.contrib import admin
from .models import Description, Bill, Customer, Sale

# Register your models here.
admin.site.register(Description)
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(Sale)
