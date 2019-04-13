from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicListView.as_view(), name="vote-list"),
    # path('/create', views.TopicCreateView.as_view(), name="vote-list"),
    # path('/<int:pk>', views.RoomDetail.as_view(), name='room-detail'),
]