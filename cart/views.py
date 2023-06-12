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


def update_cart(request, product_id):
    """Add or Remove itens from cart"""
    quantity = int(request.POST.get('quantity')or 0)
    if quantity == 0:  
        messages.warning(request,'Enter a new Quantity or Proceed to Checkout!')
    else:
        cart = request.session.get('cart',{})
        products = Products.objects.all()
        if quantity >= 0:
            cart[product_id] = quantity
            messages.success(request,'Your cart was updated sucessfully!')
        else:
            cart.pop(product_id)
        request.session['cart'] = cart
    return redirect(reverse('cart'))


def delete_cart(request, product_id):
    quantity = int(request.POST.get('quantity')or 0)
    cart = request.session.get('cart',{})
    products = Products.objects.all()
    if quantity >= 0:
        cart.pop(product_id)
        request.session['cart'] = cart
        messages.success(request,'Item removed from your Cart!')
    return redirect(reverse('cart'))