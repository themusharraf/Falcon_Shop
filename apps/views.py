from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from apps.forms import UsersCreationForm, ProductForm
from apps.models import Product


def homepage(request):
    return render(request, 'index.html')


def register(request):
    context = {
        'form': UsersCreationForm()
    }
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['form'] = form
    return render(request, 'auth/register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user is not None:
            login(request, user)
            return redirect('products')
    return render(request, 'auth/login.html')


def forgot(request):
    return render(request, 'auth/forgot-password.html')


def logout_page(request):
    logout(request)
    return render(request, 'auth/logout.html')


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/product-grid.html', context)


def product_details(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/product-details.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'product/add_product.html')


# Apple MacBook Pro (15" Retina, Touch Bar, 2.2GHz 6-Core Intel Core i7, 16GB RAM, 256GB SSD) - Space Gray (Latest Model)
# Testing conducted by Apple in October 2018 using pre-production 2.9GHz 6‑core Intel Core i9‑based 15-inch MacBook Pro systems with Radeon Pro Vega 20 graphics, and shipping 2.9GHz 6‑core Intel Core i9‑based 15‑inch MacBook Pro systems with Radeon Pro 560X graphics, both configured with 32GB of RAM and 4TB SSD.