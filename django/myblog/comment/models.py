from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

# Create your models here.


class Comment(models.Model):
    # 外键指向contenttype
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 对应模型主键值
    object_id = models.PositiveIntegerField()
    # 把以上两个组合
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)  # 谁写的评论

    root = models.ForeignKey('self', related_name='root_comment', null=True,
                             on_delete=models.CASCADE)  # 每条回复基于哪条评论(顶级评论)

    # parent_id = models.IntegerField(default=0)  # 创造一个指向object_id的父键(1,2,3等等)
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.CASCADE)
    # 指向自己，没有的允许为空，相当于自关联,在admin显示Comment object(1),Comment object(2)...
    reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.CASCADE)  # 回复谁

    def __str__(self):
        return self.text  # 返回具体的评论内容23333等

    class Meta():
        ordering = ['comment_time']
