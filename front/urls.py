from django.conf.urls import url

from . import views
app_name = 'front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sale/$', views.sale, name='sale'),
    url(r'^sale/cust/$', views.commitcust, name='commitcust'),
    url(r'^sale/bill/$', views.commitsale, name='commitsale'),
    url(r'^sale/item/([0-9]+)/$', views.item),
    url(r'^sale/cust/phone/([0-9]+)/$', views.cust_phone),
    url(r'^inventory$', views.commitvalues, name='inventory'),
    url(r'^inventory/bill/$', views.commitbill, name='commitbill'),
]
