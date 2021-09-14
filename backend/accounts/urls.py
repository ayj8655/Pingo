from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('check_duplication/', views.check_duplication),
]
