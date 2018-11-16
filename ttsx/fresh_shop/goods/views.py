from django.shortcuts import render

from goods.models import Goods, GoodsCategory


def index(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        categorys = GoodsCategory.CATEGORY_TYPE
        goods_dict = {}
        for category in categorys:
            goods_list = []
            count = 0
            for good in goods:
                if count < 4:
                    if category[0] == good.category_id:
                        goods_list.append(good)
                        count += 1
            goods_dict[category[1]]=goods_list

        return render(request, 'index.html', {'goods_dict': goods_dict})


def detail(request, id):
    if request.method == 'GET':
        # 查看商品详情，返回商品对象
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'detail.html', {'goods': goods})