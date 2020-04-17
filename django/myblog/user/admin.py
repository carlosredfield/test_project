from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False  # 不允许删除


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'nickname', 'email', 'is_staff', 'is_active', 'is_superuser')

    def nickname(self, obj): #UserAdmin没有nickname，自定义出来
        return obj.profile.nickname #obj->user
    nickname.short_description = '昵称' #字段起别名


# Re-register UserAdmin
admin.site.unregister(User)				#User取消注册
admin.site.register(User, UserAdmin)	#重新注册User, UserAdmin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname')
