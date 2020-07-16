from django.urls import path
from . import views

urlpatterns = [
    path("category_list", views.category_list, name="CategoryList"),
    path("showform/", views.showform, name='showform')
]
