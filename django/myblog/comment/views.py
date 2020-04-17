from django.shortcuts import render, redirect
from .models import Comment
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .forms import CommentForm
from django.http import JsonResponse


def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))  # 返回页面
    comment_form = CommentForm(request.POST, user=request.user)  # 存入用POST请求参数的user让CommentForm获取
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存数据
        comment = Comment()  # 实例化,如果通过则写入评论
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']

        parent = comment_form.cleaned_data['parent']  # parent类似于省id
        if not parent is None:  # 如果是回复(不是评论)
            comment.root = parent.root if not parent.root is None else parent
            # not parent.root is None=回复(不是评论)说明是回复写入parent.root，是评论则写入parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()

        # 返回数据
        data['status'] = 'success'
        data['username'] = comment.user.get_nickname_or_username()
        data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
        data['text'] = comment.text
        if not parent is None:  # 如果是回复(不是评论)
            data['reply_to'] = comment.reply_to.get_nickname_or_username()
        else:  # reply_to(回复谁)
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if not comment.root is None else ''

    else:
        # return render(request, 'error.html', {'message': comment_form.errors, 'redirect_to': referer})
        data['status'] = 'error'
        data['message'] = list(comment_form.errors.values())[0][0]
    return JsonResponse(data)

    '''对比
    把之前的删除
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    # 数据检查
    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '用户未登录', 'redirect_to': referer})
    text = request.POST.get('text', '')  # 取评论内容取不到取空
    if text == '':
        return render(request, 'error.html', {'message': '评论内容为空', 'redirect_to': referer})
    try:
        content_type = request.POST.get('content_type', '')
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()  # =Blog
        model_obj = model_class.objects.get(pk=object_id)  # =Blog.objects.get()
    except Exception as e:
        return render(request, 'error.html', {'message': '评论对象不存在', 'redirect_to': referer})

    # 检查通过，保存数据
    comment = Comment()  # 实例化
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()

    return redirect(referer)
    对比完毕'''
