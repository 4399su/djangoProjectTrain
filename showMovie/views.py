import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
# Create your views here.
from showMovie.models import Movie

"""
def page(num, size=20):#顶层分页
    num = int(num)

    totalRecords = Movie.objects.filter().count()

    totalPages = math.ceil(totalRecords * 1.0 / size)

    # 判断是否越界
    if num < 1:
        return 1
    elif num > totalPages:
        return totalPages

    movies = Movie.objects.all()[((num - 1) * size):(num * size)]

    return movies, num


def showMovie(request):
    movie = Movie.objects.all()
    num = request.GET.get('num', 1)
    movie, n = page(num)
    pre_page_num = n - 1
    next_page_num = n + 1
    return render(request, 'showMovie.html',
                  {"movie": movie, 'pre_page_num': pre_page_num, 'next_page_num': next_page_num})
                  """


def showMovie(request):
    # 获取当前页码数
    num = request.GET.get("num", 1)
    n = int(num)
    movies = Movie.objects.all()
    paginator = Paginator(movies, 20)
    # 获取当前页的数据
    try:
        perpage_data = paginator.page(n)
    except PageNotAnInteger:
        # 返回第一页数据
        perpage_data = paginator.page(1)
    except EmptyPage:
        # 返回最后一页数据
        perpage_data = paginator.page(paginator.num_pages)
    begin = n - (int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages
    pagelist = range(begin, end + 1)
    return render(request, 'showMovie.html',
                  {"paginator": paginator, "perpage_data": perpage_data, "pagelist": pagelist, "currentPage": n})
