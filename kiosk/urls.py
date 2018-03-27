from django.conf.urls import url

from . import views

app_name = 'kiosk'

urlpatterns = [
    url(r'^$', views.get_products_list, name='list-product'),

    url(r'^presentation$', views.pres, name='presentation'),
]
