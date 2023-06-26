from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:id>', views.update_cart, name='update_cart'),
    path('cart/delete/<str:id>', views.delete_cart, name='delete_cart')
]