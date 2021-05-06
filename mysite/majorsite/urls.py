from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'majorsite'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_users', views.all_users, name='all_users'),
    path('showfriends', views.showfriends, name='showfriends'),
    path('show_requests', views.show_requests, name='show_requests'),
    path('id<int:id>', views.personalpage),
    path('friend/add/<slug>/', views.add_friend),
    path('friend/accept/<int:id>/', views.accept_friend),
    path('friend/reject/<int:id>/', views.reject_friend),
    path('define_avatar', views.define_avatar, name='define_avatar'),
    path('audios<int:id>', views.audios, name='audios'),
    path('audios_upload', views.audios_upload, name='audios_upload'),
    path('create_post', views.post_create, name='create_post'),
    path('accounts/', include('django.contrib.auth.urls')),
]

