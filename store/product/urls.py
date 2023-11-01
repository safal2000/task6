from django.urls import path, include
from . import views
from product import views
from django.contrib.auth import views as auth_views

app_name = 'product'

urlpatterns = [
    path('online_shop/', views.online_shop, name='online_shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('signup/', views.your_signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]

