from django.urls import path
from . import views

urlpatterns = [
    path('api/collaborate', views.PostListCreate.as_view()),
    path('api/members', views.MemberListCreate.as_view()),
]