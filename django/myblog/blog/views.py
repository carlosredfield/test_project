from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . models import Blog, BlogType
from django.db.models import Count
from readcount.util import readcount_once_read
from django.contrib.contenttypes.models import ContentType

each_page_blogs_num = 2


def get_blog_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, each_page_blogs_num)  # 每10页进行分页
    page_num = request.GET.get('page', 1)  # 获取url页码参数(GET请求)
    page_of_blogs = paginator.get_page(page_num)  # get_page方法无论输入什么abc都会返回数值类型
    current_page_num = page_of_blogs.number  # 获取当前页
    # 获取当前页码前后各两页的页码范围
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
        list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页喝尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取博客分类的对应博客数量
    blog_type_list = BlogType.objects.annotate(blog_count=Count('blog'))
    # 以下代码等同上方一行
    # blog_types = BlogType.objects.all()
    # blog_type_list = []
    # for blog_type in blog_types:
    #     blog_type.blog_count = Blog.objects.filter(blog_type=blog_type).count()
    #     blog_type_list.append(blog_type)

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year, created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    # 以下为返回给前端页面
    context = {}
   #context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blog_types'] = blog_type_list
    context['page_range'] = page_range
    context['blog_dates'] = blog_dates_dict
    return context


def blog_list(request):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(request, blogs_all_list)
    return render(request, 'blog/blog_list.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)  # 博客类型的字段
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blog_type'] = blog_type
    return render(request, 'blog/blogs_with_type.html', context)


def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)
    context = get_blog_list_common_data(request, blogs_all_list)
    context['blogs_with_date'] = '%s年%s月' % (year, month)

    return render(request, 'blog/blogs_with_date.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookies_key = readcount_once_read(request, blog)

    context = {}
    context['blog'] = blog
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    response = render(request, 'blog/blog_detail.html', context)  # 响应
    response.set_cookie(read_cookies_key, 'true')  # 阅读cookies标记
    return response