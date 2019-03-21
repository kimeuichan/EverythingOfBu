from django.urls import path
from . import views


urlpatterns = [
    path('', views.RoomListCreate.as_view(), name="room-list"),
    path('/<int:pk>', views.RoomDetail.as_view(), name='room-detail'),
]