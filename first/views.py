from django.http import HttpResponse
from django.shortcuts import render
from .models import *

list = [{'name': '1', 'password': '2'}, {'name': '3', 'password': '4'}]


# Create your views here.
def index(request):
    m = request.method
    ufo = user.objects.all()  # 返回列表
    return render(request, 'index.html', {'ufo': ufo})
    # data = {'name': name, 'password': password}
    # list.append(data)
    # return render(request, 'index.html', {'form': list})


def register(request):
    m = request.method
    if m == 'GET':
        return render(request, 'register.html')
    else:
        name = request.POST.get('name', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        # 判断非空
        if name and password1:
            # 创建模型对象
            u = user(name=name, password=password1)
            ure = user.objects.all()
            # c = user.objects.filter().count()
            for line in ure:
                if name == line.name:
                    return HttpResponse('当前已存在此账号，请重新输入')
            if password1 != password2:
                return HttpResponse('输入密码两次不一致')
            # 插入数据库
            u.save()
            return HttpResponse('注册成功')
    return HttpResponse('注册失败')


def login(request):
    # 接受请求参数
    name = request.POST.get('name', None)
    password = request.POST.get('password', None)
    c = user.objects.filter(name=name, password=password).count()  # 返回列表个数
    if name != "" and password != "":
        if c == 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账户或密码不匹配")
    else:
        return HttpResponse("账户或密码为空")
