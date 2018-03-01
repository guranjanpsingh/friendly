from django.urls import path
from .views import users

urlpatterns = [
    path("users", users.UsersView.as_view())
]