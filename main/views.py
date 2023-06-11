from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, CartForm, CreditCardForm
from .models import FoodProduct, Cart, Favorite, Order, CartObs, Categoria
from django.contrib.auth.decorators import login_required
from pixqrcode import PixQrCode
from django.db.models import Sum, F
from datetime import datetime, timedelta
from django.contrib import messages
from django.utils import timezone

def login(request):
    login_error_message = None
    registration_error_message = None

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            username = request.POST.get('Username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                print("User is authenticated")
                return redirect('home')
            else:
                print("User is not authenticated")
                login_error_message = "Invalid login credentials. Please try again."
                form_to_show = 'signup'

        elif form_type == 'signup':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                print("User is created")
                return redirect('login')
            else:
                registration_error_message = "Invalid sign up information. Please try again."
                print("User is not created")
                print(form.errors)

    form = SignUpForm()
    return render(request, 'login.html', {'form': form, 'login_error_message': login_error_message, 'registration_error_message': registration_error_message})

@login_required(login_url='login')
def catalog(request):
    pesquisa = request.GET.get('search', '')
    categoria = request.GET.get('categoria', '')
    if pesquisa:
        food_product = FoodProduct.objects.filter(name__icontains=pesquisa)
    elif categoria:
        food_product = FoodProduct.objects.filter(categoria__categoria=categoria)
    else:
        food_product = FoodProduct.objects.all()
    
    todas_categorias = Categoria.objects.all()
    return render(request, 'catalog.html', {'food_products': food_product, 'todas_categorias': todas_categorias})



@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, product=product, defaults={'quantity': 0})

    selected_quantity = int(request.POST.get('quantity', 1))

    if not created:
        cart.quantity += selected_quantity
        messages.success(request, "Seu produto foi adicionado ao carrinho!")
    else:
        cart.quantity = selected_quantity

    cart.save()

    return redirect('home')



@login_required(login_url='login')
def product_detail_view(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    quant, created = Cart.objects.get_or_create(user=request.user, product=product)
    context = {'product': product, 'quant': quant}
    return render(request, 'product_detail.html', context)

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart_item = get_object_or_404(Cart, user=request.user, product=product)
    cart_item.delete()
    messages.success(request, 'Seu produto foi removido com sucesso!')
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
    
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            text_box_obs_value = form.cleaned_data.get('text_box_obs', '')
            if not text_box_obs_value:
                text_box_obs_value = 'nenhuma'
            
            # Salvar a observação do usuário no modelo CartObs
            cart_obs = CartObs(user=request.user, text_box_obs=text_box_obs_value)
            cart_obs.save()
            
            
            return redirect('payment')
    else:
        form = CartForm()
        
    context = {
        'cart_items_total': cart_items_total,
        'cart_total': cart_total,
        'form': form,
    }

    return render(request, 'cart.html', context)

@login_required(login_url='login')
def increment_quantity_prod_detail(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    product = Cart.objects.get(user=request.user, product=product)
    if product.quantity < 9:
        product.quantity += 1
        product.save()
    return redirect( 'product_detail', product_id=product_id)

@login_required(login_url='login')
def decrement_quantity_prod_detail(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    product = Cart.objects.get(user=request.user, product=product)
    if product.quantity > 1:
        product.quantity -= 1
        product.save()
    return redirect( 'product_detail', product_id=product_id )

@login_required(login_url='login')
def order_status(request):
    return render(request, 'order_status.html')

@login_required(login_url='login')
def generate_qr_code(request):
    name = 'Ana'
    mobile = '(81)992867651'
    city = 'Recife'

    cart_items = Cart.objects.filter(user=request.user)

    total = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total']

    if total is None:
        return render(request, 'payments/error.html', {'message': 'Cart is empty'})

    total_str = format(float(total), '.2f')

    pix = PixQrCode(name, mobile, city, total_str)

    if pix.is_valid():
        qr_base64 = pix.export_base64()
        return render(request, 'qr_code.html', {'qr_base64': qr_base64})
    else:
        return render(request, 'error.html', {'message': 'Invalid input fields'})


def payment(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_obs = CartObs.objects.filter(user=request.user).latest('id')
    total = cart_items.aggregate(total=Sum(F('product__price') * F('quantity')))['total']
    total_str = format(float(total), '.2f') if total is not None else '0.00'

    if request.method == 'POST':
        payment_method = request.POST.get('payment-method')
        pickup_time_str = request.POST.get('pickup-time')

        order_datetime = datetime.now()
        pickup_time = datetime.strptime(pickup_time_str, "%H:%M") if pickup_time_str else None
        order_products = [f"{item.quantity}x {item.product.name}" for item in cart_items]
        order_summary = ", ".join(order_products)
        

        order = Order(user=request.user, order=order_summary,           order_datetime=order_datetime,
                      pickup_time=pickup_time, total=total, payment_method=payment_method, obs = cart_obs.text_box_obs, order_status= "active" )
        order.save()

        if payment_method == 'pix':
            return redirect('generate_qr_code')
        if payment_method == 'credit-card':
            return redirect('credit_card')

    return render(request, 'payment.html', {'total': total_str})


@login_required(login_url='login')
def order_status(request):
    cart = Cart.objects.filter(user=request.user)
    cart_obs = CartObs.objects.filter(user=request.user).last()
    order = Order.objects.filter(user=request.user).last()
    order_history = Order.objects.filter(user=request.user).order_by('-order_datetime')

    if request.method == 'POST':
        if 'finishorder' in request.POST:
            order.order_status = "finished"
            order.save()
            messages.success(request, 'Pedido retirado! Bom apetite!')
        else:
            messages.success(request, 'Pedido finalizado com sucesso!')
            cart.delete()
            cart_obs.delete()

        return redirect('order_status')

    context = {
        'order': order,
        'order_history': order_history,
    }
    return render(request, 'order_status.html', context)
   
@login_required(login_url='login')
def add_to_cart_from_detail(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.save()
    return redirect('home')

def credit_card(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_status')
        else:
            print(form.errors)
    else:
        form = CreditCardForm()
    return render(request, 'credit_card.html', {'form': form})

def cancel_order(request):
    last_order = Order.objects.filter(user=request.user).last()

    if last_order is None:
        return render(request, 'error.html', {'message': 'Não há pedidos para cancelar.'})
    
    if request.method == 'POST':
        last_order.order_status = 'cancelled'
        last_order.save()
        messages.success(request, 'Pedido cancelado com sucesso.')
        return redirect('order_status')

    order_detail = {
        'pickup_time': last_order.pickup_time,
        'payment_type': last_order.get_payment_method_display(),
        'order_detail': last_order.order,
        'order_note': last_order.obs,
        'total_value': last_order.total,
        'order_id': last_order.id,
    }

    return render(request, 'cancel_order.html', order_detail)
@login_required(login_url='login')
def finish_order(request):
    order = Order.objects.filter(user=request.user).last()
    if request.method == 'POST':
        order.order_status = "finished"
        order.save()
        messages.success(request, 'Pedido retirado, bom apetite')
    
    return redirect('order_status')
     

def list_favorite(request):
    favorite_item = Favorite.objects.filter(user=request.user)
    return render(request, 'favorite.html', {'list_favorite': favorite_item})

def add_favorite(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    favorite_item, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, "Seu produto foi adicionado aos favoritos!")
    else:
        messages.warning(request, "Esse produto já foi adicionado aos favoritos")    
    return redirect('home')

def remove_favorite(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    favorite_item = get_object_or_404(Favorite, user=request.user, product=product)
    favorite_item.delete()
    return redirect('list_favorite')
    
@login_required(login_url='login')
def add_favorite_to_cart(request, product_id):
    product = get_object_or_404(FoodProduct, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.save()
    return redirect('list_favorite')
