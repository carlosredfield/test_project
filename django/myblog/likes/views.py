from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.db.models import ObjectDoesNotExist
from .models import LikeCount, LikeRecord


def SuccessResponse(like_num):
    data = {}
    data['status'] = 'SUCCESS'
    data['like_num'] = like_num
    return JsonResponse(data)


def ErrorResponse(code, message):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['messaage'] = message
    return JsonResponse(data)


def like_change(request):
    # 从Ajax获取的数据
    user = request.user
    if not user.is_authenticated:  # 验证是否登录
        return ErrorResponse(400, '还没有登录哦')

    content_type = request.GET.get('content_type')  # 前端获取的
    object_id = int(request.GET.get('object_id'))

    try:
        content_type = ContentType.objects.get(model=content_type)  # 后端获取的
        model_class = content_type.model_class()
        model_obj = model_class.objects.get(pk=object_id)
    except ObjectDoesNotExist:
        return ErrorResponse(401, '不存在哦')

    # 处理数据
    if request.GET.get('is_like') == 'true':  # 'active'.length ==0,要点赞
        # 记录谁的点赞
        like_record, created = LikeRecord.objects.get_or_create(
            content_type=content_type, object_id=object_id, user=user)

        if created:  # 如果是新增的（之前没有点过赞）
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            like_count.like_num += 1
            like_count.save()
            return SuccessResponse(like_count.like_num)
        else:  # 点过赞已经有记录，但active为0，说明重复点赞？
            return ErrorResponse(402, '你已经点赞过了哦')
    else:  # 'active'.length !=0,取消点赞
        # 如果有点赞记录就取消点赞
        if LikeRecord.objects.filter(content_type=content_type, object_id=object_id, user=user).exists():
            like_record = LikeRecord.objects.get(content_type=content_type, object_id=object_id, user=user)
            like_record.delete()  # 清除点赞记录
            # 点赞减一
            like_count, created = LikeCount.objects.get_or_create(content_type=content_type, object_id=object_id)
            if not created:
                like_count.like_num -= 1
                like_count.save()
                return SuccessResponse(like_count.like_num)
            else:  # 有点赞记录但属于create,错误
                return ErrorResponse(404, '数据错误哦')

        else:  # 如果没有点赞记录但active处于激活状态
            return ErrorResponse(403, '没有点赞过，不能取消哦')
