from django.urls import path
from . import views


urlpatterns = [
    path('', views.RoomListCreate.as_view(), name="room_list")
]