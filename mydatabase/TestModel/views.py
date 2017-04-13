#coding=utf-8
from django.shortcuts import render, render_to_response, HttpResponse
#from django.http import HttpResponseRedirect
from django import forms
from TestModel.models import User

#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='账户', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单账户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                return render_to_response('success.html', {'username': username})
            else:
                return render_to_response('fail.html', {'username': username})
    else:
        uf = UserForm()

    return render_to_response('login.html', {'uf':uf})

def index(request):
    return HttpResponse(u"Hello Django!")

