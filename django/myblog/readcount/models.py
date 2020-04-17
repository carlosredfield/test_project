from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    # 外键指向contenttype
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # 对应模型主键值
    object_id = models.PositiveIntegerField()
    # 把以上两个组合
    content_object = GenericForeignKey('content_type', 'object_id')

 
class ReadNumExpand():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)  # Blog也行，self本身是个具体的Blog对象
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except:
            return 0

#每天的阅读
class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    #content_object = <Blog:新的一年，全新开始> = 具体的实例对象