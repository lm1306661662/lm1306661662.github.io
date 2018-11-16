from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from goods.models import Goods, GoodsCategory
from user.forms import UserRegisterForm, UserLoginForm
from user.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # 2. 验证数据完整性
            if not all([username, password]):
                msg = '请填写完整的登录信息'
                return render(request, 'login.html', {'msg': msg})
            user = User.objects.filter(username=username).first()
            if not user:
                msg = '该账号没有注册，请去注册'
                return render(request, 'login.html', {'msg': msg})
            if check_password(password, user.password):
                # 验证成功
                # Django自带auth模块， 签名token ， 会话上下文session
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('goods:index'))
            else:
                msg = '密码错误'
                return render(request, 'login.html', {'msg': msg})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        data = request.POST
        form = UserRegisterForm(data)
        if form.is_valid():
            # 密码加密
            password = make_password(form.cleaned_data.get('password'))
            User.objects.create(username = form.cleaned_data.get('username'),
                                password = password,
                                email = form.cleaned_data.get('email')
                                )
            return HttpResponseRedirect(reverse('user:login'))
        else:
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})


def logout(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'login.html')