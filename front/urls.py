from django.conf.urls import url

from . import views
app_name = 'front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$',views.home, name='home'),
    url(r'^sale/$', views.sale, name='sale'),
    url(r'^sale/date/$',views.custdate, name="custdate"),
    url(r'^purchase/date/$',views.purchasedate, name="purchasedate"),
    url(r'^sale/item/([0-9]+)/$', views.item),
    url(r'^sale/cust/phone/([0-9]+)/$', views.cust_phone),
    url(r'^sale/bills/$', views.custbill, name='custbill'),
    url(r'^sale/cust/$', views.commitcust, name='commitcust'),
    url(r'^sale/bill/$', views.commitsale, name='commitsale'),
    url(r'^sale/item/$', views.items,name='viewitems'),
    url(r'^sale/cust/phone/$', views.cust_phones,name='phoney'),
    url(r'^inventory$', views.commitvalues, name='inventory'),
    url(r'^inventory/bill/$', views.commitbill, name='commitbill'),
]
