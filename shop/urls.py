from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product-detail/<int:product_id>', views.product_detail, name='product_detail')
]