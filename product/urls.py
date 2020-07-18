from django.urls import path
from . import views

urlpatterns = [
    path("category-list/", views.category_list, name="category_list"),
    path("category-create/", views.category_create, name='category_create'),
    path('product-create/', views.ProductCreateView.as_view(), name='product_create'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='detail')
]
