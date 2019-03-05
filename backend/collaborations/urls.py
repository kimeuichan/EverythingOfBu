from django.urls import path
from . import views

urlpatterns = [
    path('api/collaborate/post', views.PostListCreate.as_view()),
    path('api/collaborate/post/<int:pk>', views.PostDetail.as_view()),
    path('api/collaborate/member', views.MemberListCreate.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]