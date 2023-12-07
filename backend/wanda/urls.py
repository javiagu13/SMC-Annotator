from django.urls import path
from . import views

urlpatterns = [
                path('modify_file/', views.modify_file)
]