import datetime
from django.shortcuts import render, redirect  # 跳转方法
from django.contrib.contenttypes.models import ContentType
from readcount.util import get_sevendays_readdate, get_today_hotdata, get_yesterday_hotdata
from blog.models import Blog
from django.urls import reverse
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache


def get_sevenday_hotdata():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects \
        .filter(read_details__date__lt=today, read_details__date__gte=date)\
        .values('id', 'title') \
        .annotate(read_num_sum=Sum('read_details__read_num')) \
        .order_by('-read_num_sum')
    return blogs[:7]


'''
    blogs.values('id','title')#7天内的每一篇阅读
    ->[('id':16,'title':'for 16'),('id':16,'title':'for 16'),('id':16,'title':'for 16'),('id':15,'title':'for 15')......]
    .annotate(Sum('read_details__read_num'))
    ->[('id':16,'title':'for 16','read_details__read_num__sum':5),('id':15,'title':'for 15','read_details__read_num__sum':3)......]
'''


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_sevendays_readdate(blog_content_type)

    # 获取7天热门博客的缓存数据
    sevenday_hot_data = cache.get('sevenday_hot_data')
    if sevenday_hot_data is None:
        sevenday_hot_data = get_sevenday_hotdata()
        cache.set('sevenday_hot_data', sevenday_hot_data, 3600)
    #     print('cal')
    # else:
    #     print('use cache')

    context = {}
    context['read_nums'] = read_nums
    context['dates'] = dates
    context['today_hot_data'] = get_today_hotdata(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hotdata(blog_content_type)
    context['sevenday_hot_data'] = sevenday_hot_data
    return render(request, 'home.html', context)
