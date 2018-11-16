from django.conf.urls import url

from cart import views

urlpatterns = [
url(r'^cart/', views.cart, name='cart'),
url(r'^add_cart/', views.add_cart, name='add_cart'),
url(r'^place_order/', views.place_order, name='place_order'),
url(r'^delete/', views.delete, name='delete'),
url(r'^f_price/', views.f_price, name='f_price'),
url(r'^cart_count/', views.cart_count, name='cart_count'),
url(r'^change_goods_num/', views.change_goods_num, name='change_goods_num'),
]