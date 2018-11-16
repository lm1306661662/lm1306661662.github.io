from django import forms

from user.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, error_messages={'max_length': '用户名长度不能大于20',
                                                                             'required': '用户名不能为空'
                                                                             })
    password = forms.CharField(max_length=255,error_messages={'max_length': '密码长度不能大于255'})
    cpassword = forms.CharField(max_length=255,error_messages={'max_length': '密码长度不能大于255'})
    email = forms.EmailField(max_length=100, error_messages={'max_length':'邮箱长于不能大于100'})

    def clean(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError({'username': '该用户已经被注册，请重新注册'})
        if self.cleaned_data['password'] != self.cleaned_data['cpassword']:
            raise forms.ValidationError({'password': '两次输入的密码不一致'})
        return self.cleaned_data


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20, required=True, error_messages={'max_length': '用户名长度不能大于20',
                                                                             'required': '用户名不能为空'
                                                                             })
    password = forms.CharField(max_length=255, error_messages={'max_length': '密码长度不能大于255'})
    cpassword = forms.CharField(max_length=255, error_messages={'max_length': '密码长度不能大于255'})
    email = forms.EmailField(max_length=100, error_messages={'max_length': '邮箱长于不能大于100'})

    def clean(self):
        # 先判断用户是否注册
        user = User.objects.filter(username=self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username': '该用户名没有被注册，请去注册'})
        return self.cleaned_data