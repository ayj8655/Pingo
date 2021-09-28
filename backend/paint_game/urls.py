from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('make_room/', views.make_room),
    path('room_member/<int:room_id>/', views.room_member),
    path('room_list/', views.room_list),
    path('enter_room/', views.enter_room),
<<<<<<< HEAD
    path('image/', views.canvasToImage),
    # path('saving/', views.saving),
=======
    path('saving/', views.saving),
>>>>>>> 72d8a620c4ae0ac780b83e1f5b188a2f15be1922
    path('<str:room_name>/', views.room, name='room'),
]