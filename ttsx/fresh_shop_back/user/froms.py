from django import forms
from django.contrib.auth.models import User


class UserLoginFrom(forms.Form):
    username = forms.CharField(max_length=10, required=True,
                               error_messages={'required':'账号必填',
                                               'max_length':'不能超过10个字符'
                                               })
    password = forms.CharField(required=True,
                               error_messages={
                                               'max_length': '不能超过10个字符'
                                               })
    def clean(self):

        user = User.objects.filter(username = self.cleaned_data.get('username'))
        if not user:
            raise forms.ValidationError({'username': '该账号没有注册，请去注册'})
        return self.cleaned_data