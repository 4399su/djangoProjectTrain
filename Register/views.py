from django.http import HttpResponse
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
        flag = registerStu(sname, cname, *coname)
        if flag:
            return HttpResponse("注册成功")
        else:
            return HttpResponse("注册失败")


def showall(request):
    cl = Clazz.objects.all()
    count = 0
    return render(request, 'showall.html', {"cl": cl})


def showdetail(request):
    clnumber = request.GET.get('clnumber')
    clnumber = int(clnumber)
    st = Clazz.objects.get(clnumber=clnumber).student_set.all()
    return render(request, 'showdetail.html', {"st": st})
