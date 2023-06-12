from django.shortcuts import get_object_or_404
from products.models import Products, Category


def cart_products(request):
    """
    Show the numbers of items in cart in all pages if user are log in
    """
    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    number_of_items = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Products, pk=product_id)
        total += quantity * product.price
        number_of_items += quantity
       
        cart_items.append({'product_id':product_id, 'quantity':quantity, 'product':product})
    return {'cart_items': cart_items, 'total': total, 'number_of_items': number_of_items}  
