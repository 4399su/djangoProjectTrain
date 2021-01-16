from django.shortcuts import render
from .models import *


# Create your views here.
def show(request):
    if request.method == 'GET':
        return render(request, 're.html')
    else:
        sname = request.POST.get("sname", None)
        cname = request.POST.get("cname", None)
        # 复选框接收列表
        coname = request.POST.getlist("coname", [])

        # 注册到数据库
        registerStu(sname, cname, *coname)
        return None
