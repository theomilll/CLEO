from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import FoodProduct, Cart, Favorite
from django.contrib.auth.decorators import login_required

def login(request):
    error_message = None

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                print("User is authenticated")
                return redirect('home')
            else:
                print("User is not authenticated")
                error_message = "Invalid login credentials. Please try again."

        elif form_type == 'signup':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                print("User is created")
                return redirect('login')
            else:
                error_message = "Invalid sign up information. Please try again."
                print("User is not created")
                print(form.errors)
            error_message = "Invalid request."

    form = SignUpForm()
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

@login_required(login_url='login')
def catalog(request):
    food_products = FoodProduct.objects.all()
    return render(request, 'catalog.html', {'food_products': food_products})

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart.quantity += 1
        cart.save()
    return redirect('home')

@login_required(login_url='login')
def product_detail_view(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    #detail_name = product.objects.name
    
    return render(request, 'product_detail.html', {})

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart_item = get_object_or_404(Cart, user=request.user, product=product)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='login')
def increment_quantity(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    product = Cart.objects.get(user=request.user, product=product)
    if product.quantity < 9:
        product.quantity += 1
        product.save()
    return redirect('cart')

@login_required(login_url='login')
def decrement_quantity(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    product = Cart.objects.get(user=request.user, product=product)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect('cart')

@login_required(login_url='login')
def clear_cart(request):
    Cart.objects.filter(user=request.user).delete()
    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_items_total = []
    
    for item in cart_items:
        total = item.product.price * item.quantity
        cart_items_total.append((item, total))
    
    cart_total = sum([total for _, total in cart_items_total])
    
    context = {
        'cart_items_total': cart_items_total,
        'cart_total': cart_total,
    }

    return render(request, 'cart.html', context)
