from django.conf.urls import url

from . import views
app_name = 'front'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bills/$', views.bill, name='bills'),
    url(r'^commit/$', views.commitvalues, name='commit'),
]
