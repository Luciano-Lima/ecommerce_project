from django.shortcuts import render, redirect, reverse
from products.models import Products
from django.contrib import messages

# Create your views here.
# Render the home page for cart
def cart(request):
    return render(request, 'cart.html')

#Add item to cart 
def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity') or 0)#prevents literal for int() error
    if quantity == 0:
        messages.warning(request,'Please enter a quantity!')
        
    cart = request.session.get('cart', {})
    if product_id in cart:
        cart[product_id] = int(cart[product_id]) + quantity      
    else:
        cart[product_id] = cart.get(product_id, quantity) 
    request.session['cart'] = cart
    return redirect(reverse('home'))
