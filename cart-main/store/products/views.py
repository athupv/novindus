from django.shortcuts import render,HttpResponse,redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.
@login_required
def product(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }
    return render(request, 'products/products.html', context=context)

@login_required
def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:products')  
    else:
        form = ProductForm()
    
    return render(request, 'products/add_products.html', {'form': form})