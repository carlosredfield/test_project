from django.shortcuts import render, redirect  # 跳转方法
from django.contrib import auth
from django.urls import reverse
from .forms import LoginForm, RegForm, ChangeNickNameForm, BindEmailForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Profile
from django.core.mail import send_mail
import string
import random
import time

def login_for_modal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():  # 验证通过
        user = login_form.cleaned_data['user']  # 获取user
        auth.login(request, user)  # 登录
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'

    return JsonResponse(data)


def login(request):
    if request.method == 'POST':  # post请求，即在登录页面点登录提交所输入的数据
        login_form = LoginForm(request.POST)  # 带有已经提交的数据
        if login_form.is_valid():  # 验证通过
            user = login_form.cleaned_data['user']  # 获取user
            auth.login(request, user)  # 登录
            return redirect(request.GET.get('from', reverse('home')))
            # 返回到有from这个参数的页面，如果找不到就返回到home页面

    else:  # get请求，即进入登录页面
        login_form = LoginForm()  # 实例化，创建一个对象，不带有已经提交的数据

    context = {}
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

    '''对比
    username = request.POST.get('username', '')  # 获取不到就为空
    password = request.POST.get('password', '')  # 获取不到就为空
    user = auth.authenticate(request, username=username, password=password)
    referer = request.META.get('HTTP_REFERER',reverse('hmoe'))
                            #refer之前的页面，找不到就返回首页
    if user is not None:
        auth.login(request, user)
        return redirect(referer)  
    else:
        return render(request, 'error.html', {'message': '用户名或密码不正确'})
    '''


def register(request):
    if request.method == 'POST':  # post请求，即在登录页面点登录提交所输入的数据
        reg_form = RegForm(request.POST)  # 带有已经提交的数据
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 第一种
            user = User.objects.create_user(username, email, password)
            user.save()
            '''第二种实例化
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()'''

            # 注册完登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)  # 登录
            return redirect(request.GET.get('from', reverse('home')))
            # 返回登录前页面
    else:  # get请求，即进入注册页面
        reg_form = RegForm()  # 实例化，创建一个对象，不带有已经提交的数据

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('home')))


def user_info(request):
    context = {}
    return render(request, 'user/user_info.html', context)


def change_nickname(request):
    redirect_to = request.GET.get('from', reverse('home'))  # 跳转地址

    if request.method == 'POST':
        form = ChangeNickNameForm(request.POST, user=request.user)
        if form.is_valid():  # 验证通过
            nickname_new = form.cleaned_data['nickname_new']
            profile, created = Profile.objects.get_or_create(user=request.user)
            profile.nickname = nickname_new
            profile.save()
            return redirect(redirect_to)  # 保存后跳转到这个地址
    else:  # GET请求
        form = ChangeNickNameForm()

    context = {}
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_text'] = '修改'
    context['return_back_url'] = redirect_to
    context['form'] = form
    return render(request, 'form.html', context)


def bind_email(request):  # 处理邮箱表单
    redirect_to = request.GET.get('from', reverse('home'))  # 跳转地址

    if request.method == 'POST':
        form = BindEmailForm(request.POST, request=request)
        if form.is_valid():  # 验证通过
            email = form.cleaned_data['email']
            request.user.email = email  #保存Email数据
            request.user.save()
            return redirect(redirect_to)  # 保存后跳转到这个地址
    else:  # GET请求
        form = BindEmailForm()

    context = {}
    context['page_title'] = '绑定邮箱'
    context['form_title'] = '绑定邮箱'
    context['submit_text'] = '绑定'
    context['return_back_url'] = redirect_to
    context['form'] = form
    return render(request, 'user/bind_email.html', context)


def send_vercode(request):  # 发送邮件
    email = request.GET.get('email', '')
    data = {}

    if email != '':
        # 生成验证码
        code = ''.join(random.sample(string.ascii_letters + string.digits, 4))
        #后端设置30秒内不能再次发送验证码
        now = int(time.time())
        send_code_time = request.session.get('send_code_time',0)

        if now - send_code_time < 30:
            data['status'] = 'ERROR'
        else:
            request.session['bind_email_code'] = code
            request.session['send_code_time'] =now
            # 发送邮件
            send_mail(
                '绑定邮箱',  # 主题
                '验证码：%s' % code,  # 内容
                '380983372@qq.com',  # 发送者
                [email],  # 接受者
                fail_silently=False,  # 默认
            )
            data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)
