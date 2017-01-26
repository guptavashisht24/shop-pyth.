from django.conf.urls import url

from . import views
app_name = 'front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home, name='home'),
    url(r'^sale/$', views.sale, name='sale'),
    url(r'^home/sale/date/([0-9-]+)/$', views.custdate),
    url(r'^home/purchase/date/([0-9-]+)/$', views.purchasedate),
    url(r'^sale/item/([0-9]+)/$', views.item),
    url(r'^sale/cust/phone/([0-9]+)/$', views.cust_phone),
    url(r'^home/sale/bills/([0-9]+)/$', views.custbill),
    url(r'^sale/cust/$', views.commitcust, name='commitcust'),
    url(r'^sale/bill/$', views.commitsale, name='commitsale'),
    url(r'^home/sale/item/([0-9]+)/$', views.items),
    url(r'^sale/discount/$', views.discount),
    url(r'^home/sale/cust/phone/([0-9]+)/$', views.cust_phones),
    url(r'^inventory$', views.commitvalues, name='inventory'),
    url(r'^inventory/bill/$', views.commitbill, name='commitbill'),
]
