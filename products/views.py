from django.shortcuts import render
from products.models import Products, Category


# Create your views here.
def home(request):
    products = Products.objects.all().order_by('name')
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html')