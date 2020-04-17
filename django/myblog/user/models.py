from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 一个用户对应一个昵称
    nickname = models.CharField(max_length=20, verbose_name='昵称')  # 拓展nickname

    def __str__(self):
        return '<Profile:%s for %s>' % (self.nickname, self.user.username)


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


def get_nickname_or_username(self):#有昵称显示昵称，无昵称显示用户名
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return self.username


User.get_nickname = get_nickname
User.get_nickname_or_username = get_nickname_or_username
