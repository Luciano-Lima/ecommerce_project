from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>', views.categories, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>', views.productDetail, name='product_detail'),
]