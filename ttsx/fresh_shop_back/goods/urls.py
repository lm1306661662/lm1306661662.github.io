from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^goods_category_list/', views.goods_category_list, name='goods_category_list'),
    url(r'^goods_category_detail/(\d+)/', views.goods_category_detail, name='goods_category_detail'),
    # 商品列表
    url(r'^goods_list/', views.goods_list, name='goods_list'),
    # 商品添加
    url(r'^goods_add/', views.goods_add, name='goods_add'),
    # 更新商品
    url(r'^goods_update/(\d+)', views.goods_update, name='goods_update'),
    # 商品删除
    url(r'^goods_delete/(\d+)', views.goods_delete, name='goods_delete'),
    # 商品描述
    url(r'^goods_desc/(\d+)', views.goods_desc, name='goods_desc'),
]