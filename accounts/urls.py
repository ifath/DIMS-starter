from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('user_register/', views.user_register, name="user_register"),
    path("login/", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("password_reset", views.password_reset, name="password_reset")
]
