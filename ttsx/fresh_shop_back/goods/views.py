from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from goods.forms import GoodsForm
from goods.models import GoodsCategory, Goods


def goods_category_list(request):
    if request.method == 'GET':
        categorys = GoodsCategory.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_list.html', {'categorys':categorys,'types':types})


def goods_category_detail(request, id):
    if request.method == 'GET':
        # 返回商品分类对象，和分类枚举信息
        category = GoodsCategory.objects.filter(pk=id).first()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_detail.html', {'category': category, 'types': types})
    if request.method == 'POST':
        img = request.FILES.get('category_front_image')
        if img:
            # GoodsCategory.objects.filter().update()
            category = GoodsCategory.objects.filter(pk = id ).first()
            category.category_front_image = img
            category.save()
            return HttpResponseRedirect(reverse('goods:goods_category_list'))
        else:
            error = '图片必填'
            return render(request, 'goods_category_detail.html', {'error':error})


def goods_list(request):
    if request.method == 'GET':
        try:
            page = int(request.GET.get('page', 1))
        except Exception as e:
            page = 1
        # TODO :查看所有的商品信息，并在goods_list.html
        goods = Goods.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        paginator = Paginator(goods, 3)
        page_goods = paginator.page(page)
        return render(request, 'goods_list.html', {'page_goods': page_goods, 'types': types})


def goods_add(request):
    if request.method == 'GET':
        # TODO:页面中刷新分页信息
        categorys = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_detail.html', {'categorys':categorys})

    if request.method == 'POST':
        # TODO: 验证商品信息的完整性，数据的保存
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # category = form.cleaned_date.get('category')
            Goods.objects.create(**data)
            return HttpResponseRedirect(reverse('goods:goods_list'))
        else:
            # 验证失败
            errors = form.errors
            return render(request, 'goods_detail.html', {'errors':errors})


def goods_update(request, id):
    if request.method == 'GET':
        # 编辑商品对象
        types = GoodsCategory.CATEGORY_TYPE
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'goods_update.html', {'goods': goods, 'types':types})
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # 把图片从data中删掉
            # img 表示更新商品时，选择了图片，则img为图片内容
            # 如果更新的时候，没有选择图片，则img为None
            img = data.pop('goods_front_image')
            Goods.objects.filter(pk=id).update(**data)
            if img:
                goods = Goods.objects.filter(pk=id).first()
                goods.goods_front_image = img
                goods.save()
            return HttpResponseRedirect(reverse('goods:goods_list'))
        else:
            goods = Goods.objects.filter(pk=id).first()
            types = GoodsCategory.CATEGORY_TYPE
            errors = form.errors
            return render(request, 'goods_update.html', {'errors': errors, 'goods': goods, "types": types})


def goods_delete(request, id):
    if request.method == 'POST':
        # 删除商品数据，使用ajax
        Goods.objects.filter(pk=id).delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})


def goods_desc(request, id):
    if request.method == 'GET':
        # TODO: 返回商品对象，
        goods = Goods.objects.filter(pk=id).first()
        return render(request, 'goods_desc.html', {'goods':goods})
    if request.method == 'POST':
        content = request.POST.get('content')
        goods = Goods.objects.filter(pk=id).first()
        goods.goods_desc = content
        goods.save()
        return HttpResponseRedirect(reverse('goods:goods_list'))