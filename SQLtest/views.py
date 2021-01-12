from django.shortcuts import render

# Create your views here.
from showMovie.models import Movie


def showSQL(request):
    # 单表查询

    # 查询数量
    number = Movie.objects.count()

    # 条件查询 返回对象 不能为空
    Id_150 = Movie.objects.get(mid="150")

    # 条件查询 返回列表 可以为空
    Id_150copy = Movie.objects.filter(mid="150")

    # 返回第一项
    first_data = Movie.objects.first()

    # 返回最后一项
    last_data = Movie.objects.last()

    # 多表查询

    # 查询所有
    searchAll_list = Movie.objects.all()

    # 切片查询
    slice_list = Movie.objects.all()[20:40]

    # 模糊查询开头
    part_first_list = Movie.objects.filter(mname__startswith='爱情')

    # 模糊查询结尾
    part_last_list = Movie.objects.filter(mname__endswith='爱情')

    # 模糊查询包含
    part_contain_list = Movie.objects.filter(mname__contains='爱情')

    # 不区分大小写模糊查询
    Ilist = Movie.objects.filter(mname__istartswith='H')

    # 升序
    up_list = Movie.objects.order_by('mid')

    # 降序
    decreas_list = Movie.objects.order_by("-mid")

    # 部分查询
    part_attribute = Movie.objects.values("mid", "mname").filter(mname__contains='爱情')

    # 排除一部分
    exclude_list = Movie.objects.filter(mname__contains='爱情').exclude(mname__startswith='爱情')

    # 查询大于147的电影 lt小于
    gt_list = Movie.objects.filter(mid__gt='147')

    # 查询大于等于147的电影
    gte_list = Movie.objects.filter(mid__gte='147')

    # 147或150
    in_list = Movie.objects.filter(mid__in=(147, 150))

    # 147到150
    range_list = Movie.objects.filter(mid__range=(147, 150))

    # 增加
    # 1.创建对象,对象.save
    # 2.Movie.objects.create(属性赋值)

    # 修改
    # 1.获取对象，修改某一字段，对象.save
    # 2.Movie.objects.filter(条件).update(更新)

    # 删除 方式不同
    # 1. 获取对象，delete对象
    # 2. Movie.objects.filter(条件).delete()

    # 左连接

    # 右连接

    # 一对一 OneToOneField
    # 一对多 ForeighKey
    # 多对多 ManyToMany
    return render(request, "showSQL.html",
                  {"searchAll_list": searchAll_list, "number": number, "Id_150": Id_150, "Id_150copy": Id_150copy,
                   "first_data": first_data, "last_data": last_data, "slice_list": slice_list,
                   "part_first_list": part_first_list,
                   "part_last_list": part_last_list, "part_contain_list": part_contain_list, "Ilist": Ilist,
                   })
