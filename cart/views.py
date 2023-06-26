from django.shortcuts import render, redirect, reverse
from products.models import Products
from django.contrib import messages

# Create your views here.
def cart(request):
    """Render the cart page"""
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add items to cart"""
    quantity = int(request.POST.get('quantity') or 0)
    if quantity == 0:
        messages.warning(request,'Please enter a quantity!')
        
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 
    request.session['cart'] = cart
    return redirect(reverse('home'))
        

def update_cart(request, id):
    """Add or Remove itens from the cart"""
    quantity = int(request.POST.get('quantity')or 0)#prevents literal for int() error
    if quantity == 0:  
        messages.warning(request,'Enter a new Quantity or Proceed to Checkout!')
        # return redirect(reverse('checkout'))
    else:
        cart = request.session.get('cart',{})
        products = Products.objects.all()

        if quantity >= 0:
            cart[id] = quantity
            messages.success(request,'Your cart was updated sucessfully!')
        else:
            cart.pop(id)
        request.session['cart'] = cart
    return redirect(reverse('cart'))

def delete_cart(request, id):
    cart = request.session.get('cart', {})
    quantity = cart[id] - 1 #decreases the cart quantity until deletes from cart

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    request.session['cart'] = cart
    messages.success(request,'Item removed from your Cart!')
    if not cart: #if all products be deleted from cart return to destination page
        return redirect(reverse('cart'))
    return redirect(reverse('cart'))