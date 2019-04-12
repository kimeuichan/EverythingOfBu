from django.urls import path
from . import views


urlpatterns = [
    path('', views.TopicList.as_view(), name="vote-list"),
    # path('/<int:pk>', views.RoomDetail.as_view(), name='room-detail'),
]