from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart/add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>', views.update_cart, name='update_cart'),
    path('cart/delete/<int:product_id>', views.delete_cart, name='delete_cart')
]