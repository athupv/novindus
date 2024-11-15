from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart

# Create your views here.
@login_required
def cart(request):
    items = Cart.objects.filter(user=request.user)

   
    grand_total = sum(item.total_price() for item in items)

    context = {
        'items':items,
        'grand_total': grand_total,
       
    }
    return render(request, 'cart/cart.html',context=context)

@login_required
def cart_add(request, product_id):
    print("cart add")
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        # If the product is already in the cart, increase quantity by 1
        cart_item.quantity += 1
        cart_item.save()
    return redirect('products:products')  
  
@login_required
def cart_increment(request, id):
    item = get_object_or_404(Cart, id=id)
    item.quantity += 1
    item.save()
    return redirect('cart:cart')

@login_required
def cart_decrement(request, id):
    # Get the cart item by ID
    item = get_object_or_404(Cart, id=id)
    # Decrease the quantity by 1, if quantity is greater than 1
    if item.quantity > 1:
        item.quantity -= 1
        # Save the item
        item.save()
    else:
        # Optionally, can remove the item from the cart if quantity is 1
        item.delete()
    # Redirect back to the cart page
    return redirect('cart:cart')

@login_required
def remove(request,id):
    item = get_object_or_404(Cart, id=id)
    item.delete()
    return redirect('cart:cart')
    