from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('category/<slug:category_slug>/', views.ProductView.as_view(), name='category_filter'),
    path('bucket/', views.AdminHomeView.as_view(), name='bucket'),
    path('<str:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('bucket/delete/<str:pk>/', views.AdminProductDelete.as_view(), name='delete-product-admin'),

]