from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm

register = template.Library()


@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()


@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    form = CommentForm(
        initial={'content_type': content_type.model, 'object_id': obj.pk, 'reply_comment_id': 0})
    # CommentForm实例化再初始化存入content_type，object_id来携带，顶级评论表单'reply_comment_id'=0
    return form


@register.simple_tag
def get_comment_list(obj):  # 顶级评论root
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)  # 只是评论没有回复
    return comments.order_by('-comment_time')  # 顶级评论倒序排序
