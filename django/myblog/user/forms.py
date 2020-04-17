from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    username = forms.CharField(label='用户名', required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    # 接受前端传来的信息,required=True必填False可以不填，,placeholder默认显示
    password = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    # wiget加密显示,attrs={'class':'form-control')输入框样式调整

    def clean(self):  # 验证数据，执行is_vaild()方法
        username = self.cleaned_data['username']  # 获取提交的username
        password = self.cleaned_data['password']  # 获取提交的password
        # 检查是否有问题
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')  # 显示出用户名或密码不正确
        else:
            self.cleaned_data['user'] = user  # 添加user,待会从views引用
        return self.cleaned_data


class RegForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30, min_length=3, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '请输入3-30位用户名'}))
    email = forms.EmailField(label='邮箱', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password_again = forms.CharField(label='密码', min_length=6, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '请再一次输入密码'}))

    def clean_username(self):  # 验证用户名
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    def clean_email(self):  # 验证邮箱
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    def clean_password_again(self):  # 验证两次密码
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入密码不一致')
        return password_again


class ChangeNickNameForm(forms.Form):
    nickname_new = forms.CharField(label='新的昵称', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '请输入新的昵称'}))

    # 验证用户是否登录有用，目的是获取self.user
    def __init__(self, *args, **kwargs):  # 获取views存入的user,不知道父类init有什么参数，故用万金油*args, **kwargs
        if 'user' in kwargs:  # 用构造方法__init__方法会调用父类的__init__
            self.user = kwargs.pop('user')  # 故取出uesr不再储存(pop取出后不留在kwargs)
        super(ChangeNickNameForm, self).__init__(*args, **kwargs)  # 再调用父类__init__方法还原(相当于重写__init__？)

    def clean(self):
        # 前端校验用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user
        else:
            raise forms.ValidationError('用户尚未登录')
        return self.cleaned_data

    def clean_nickname_new(self):  # 前端校验数据是否为空
        nickname_new = self.cleaned_data.get('nickname_new', '').strip()
        if nickname_new == '':
            raise ValidationError('新的昵称不能为空')
        return nickname_new


class BindEmailForm(forms.Form):
    email = forms.CharField(label='邮箱', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': '请输入正确的邮箱'}))

    vercode = forms.CharField(label='验证码', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '点击“发送验证码”发送到邮箱'}))

    def __init__(self, *args, **kwargs):  # 获取views存入的request,不知道父类init有什么参数，故用万金油*args, **kwargs
        if 'request' in kwargs:  # 用构造方法__init__方法会调用父类的__init__
            self.request = kwargs.pop('request')  # 故取出request不再储存(pop取出后不留在kwargs)
        super(BindEmailForm, self).__init__(*args, **kwargs)  # 再调用父类__init__方法还原(相当于重写__init__？)

    def clean(self):
        # 前端校验用户是否登录
        if self.request.user.is_authenticated:
            self.cleaned_data['user'] = self.request.user
        else:
            raise forms.ValidationError('用户尚未登录')

        # 判断用户是否已经绑定邮箱
        if self.request.user.email != '':
            raise forms.ValidationError('你已经绑定邮箱')

        # 判断验证码
        code = self.request.session.get('bind_email_code', '')  # 发送的验证码
        vercode = self.cleaned_data.get('vercode', '')  # 用户填写的验证码
        if not (code != '' and code == vercode):
            raise forms.ValidationError('验证码不正确!')

        return self.cleaned_data

    def clean_email(self):  # 验证邮箱是否绑定
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已经被绑定')
        return email

    def clean_vercode(self):  # 验证是否为空
        vercode = self.cleaned_data.get('vercode', '').strip()
        if vercode == '':
            raise forms.ValidationError('验证码不能为空哦')
        return vercode
