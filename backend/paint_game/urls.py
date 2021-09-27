from django.urls import path
from . import views

urlpatterns = [
    path('make_room/', views.make_room),
    path('room_member/<int:room_id>/', views.room_member),
    path('room_list/', views.room_list),
    path('enter_room/', views.enter_room),
    path('image/', views.canvasToImage)
]