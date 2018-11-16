from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.froms import UserLoginFrom


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 将请求参数去给form表单做验证
        form = UserLoginFrom(request.POST)
        # 校验结果， 返回true表示校验成功
        if form.is_valid():
            user = auth.authenticate(username = form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if not user:
                # 没有user对象，表示验证密码不通过
                return render(request, 'login.html')
            # 实现登录 ，request.user等于登录系统用户对象
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:index'))
        else:
            # 验证失败返回错误信息给页面
            errors  = form.errors
            return render(request, 'login.html', {'errors': errors})

@login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')