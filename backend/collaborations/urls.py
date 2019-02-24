from django.urls import path
from . import views

urlpatterns = [
    path('api/collaborate', views.PostListCreate.as_view()),
]