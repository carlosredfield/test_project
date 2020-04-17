from django.urls import path
from . import views

# start with blog
urlpatterns = [
    path('login_for_modal/', views.login_for_modal, name='login_for_modal'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_info/', views.user_info, name='user_info'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
    path('bind_email/', views.bind_email, name='bind_email'),
    path('send_vercode/', views.send_vercode, name='send_vercode'),
]
