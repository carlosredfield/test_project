import datetime
from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from .models import ReadNum, ReadDetail
from django.utils import timezone


def readcount_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read" % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总的阅读(get_or_create返回一个元祖，用两个参数接收，created是没有用的)
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        # 计数加1
        readnum.read_num += 1
        readnum.save()

        # 每天的阅读
        date = timezone.now().date()
        readdetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readdetail.read_num += 1
        readdetail.save()
    return key


def get_sevendays_readdate(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(7, 0, -1):  # 前7天
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))  # 对read_num字段统计,得到{'read_num_sum':6}
        read_nums.append(result['read_num_sum'] or 0)  # 如果为False则写0
    return dates, read_nums

# 得到今天热门数据


def get_today_hotdata(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(
        content_type=content_type, date=today).order_by('-read_num')  # 对read_num字段倒序排序
    return read_details[:7]  # 只展示前7篇


def get_yesterday_hotdata(content_type):
    today = timezone.now().date()
    yesterday = today - datetime.timedelta(days=1)
    read_details = ReadDetail.objects.filter(
        content_type=content_type, date=yesterday).order_by('-read_num')  # 对read_num字段倒序排序
    return read_details[:7]  # 只展示前7篇

