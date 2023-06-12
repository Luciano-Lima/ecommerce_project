from django.shortcuts import render
from products.models import Products

# Create your views here.
def cart(request):
    return render(request, 'cart.html')