from django.shortcuts import render, get_object_or_404
from products.models import Products, Category


# Create your views here.
# returns all the products in the database
def home(request):
    products = Products.objects.all().order_by('name')
    # paginator = Paginator(products, 3) #display 3 items per page
    # page = request.GET.get("page", 1)
    # products = paginator.page(page)
    return render(request, "home.html", {'products': products})
    

# def about(request):
#     return render(request, 'about.html')

# Retuns all products and display to display in home page by category
def categories(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = Products.objects.filter(category=category).order_by('name')
        # paginator = Paginator(products, 3)
        # page = request.GET.get("page", 1)
        # products = paginator.page(page)
    else:
        products = Products.objects.all().filter().order_by('name')
    return render(request, "home.html", {"category": category, "products": products})

# Returns a single product
def productDetail(request, category_slug, product_slug):
    try:
        product = Products.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e: 
        raise e
    return render(request, "products.html", {"product": product})