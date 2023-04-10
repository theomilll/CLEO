from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import FoodProduct

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

def catalog(request):
    food_products = FoodProduct.objects.all()
    return render(request, 'catalog.html', {'food_products': food_products})