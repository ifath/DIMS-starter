from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    # path('user-register/', views.user_register, name="user_register"),
    path('user-register/', views.registration_view, name="registration_view"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("password_reset", views.password_reset, name="password_reset")
]
