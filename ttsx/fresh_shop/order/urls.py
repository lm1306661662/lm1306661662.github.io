from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order', views.order, name='order')
]