from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("make_room/", views.make_room),
    path("enter_room/", views.enter_room),
    path("leave_room/", views.leave_room),
    path("room_info/<int:room_id>", views.room_info),
    path("room_member/<int:room_id>/", views.room_member),
    path("room_headcount/<int:room_id>/", views.room_headcount),
    path("room_list/", views.room_list),
    path("get_categories/", views.get_categories),
    path("saving/", views.saving),
    path('paints_of_round/<int:room_id>/<str:category>', views.paints_of_round),
    path("game_end/", views.game_end),
    path("ayj/", views.ayj),
    path("<str:room_name>/", views.room, name="room"),
    path("delete_room/",views.delete_room),
    path("result_score/<int:room_id>",views.result_score),
]

