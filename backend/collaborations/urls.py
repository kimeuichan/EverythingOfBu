from django.urls import path
from . import views



urlpatterns = [
    path('api/', views.api_root),
    path('api/collaborate/post', views.PostListCreate.as_view(), name='post-list'),
    path('api/collaborate/post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('api/collaborate/member', views.MemberList.as_view(), name='member-list'),
    path('api/users', views.UserList.as_view(), name='uesr-list'),
    path('api/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]