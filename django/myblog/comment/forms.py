from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget
from .models import Comment


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(label=False, widget=CKEditorWidget(
        config_name='comment_ckeditor'), error_messages={'required': '评论内容不能为空'})
    reply_comment_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'id': 'reply_comment_id'}))
    # 回复的id，attrs={'id':'reply_comment_id'}可以通过前端页面获取

    def __init__(self, *args, **kwargs):  # 获取views存入的user,不知道父类init有什么参数，故用万金油*args, **kwargs
        if 'user' in kwargs:  # 用构造方法__init__方法会调用父类的__init__
            self.user = kwargs.pop('user')  # 故取出uesr不再储存(pop取出后不留在kwargs)
        super(CommentForm, self).__init__(*args, **kwargs)  # 再调用父类__init__方法还原(相当于重写__init__？)

    def clean(self):
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')

        # 评论对象验证
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
            # 写入然后在views获取
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')

        return self.cleaned_data

    # 验证回复是否有效(前端form校验)
    def clean_reply_comment_id(self):
        reply_comment_id = self.cleaned_data['reply_comment_id']
        if reply_comment_id < 0:
            raise forms.ValidationError('回复出错')
        elif reply_comment_id == 0:  # = 0说明是顶级评论
            self.cleaned_data['parent'] = None
        elif Comment.objects.filter(pk=reply_comment_id).exists():
            self.cleaned_data['parent'] = Comment.objects.get(pk=reply_comment_id)
        else:
            raise forms.ValidationError('回复出错')
        return reply_comment_id
