from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from apps.forms import UsersCreationForm, ProductForm
from apps.models import Product, ProductImage


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
    return render(request, 'apps/auth/register.html', context)


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user is not None:
            login(request, user)
            return redirect('product_list')
    return render(request, 'apps/auth/login.html')


def forgot(request):
    return render(request, 'apps/auth/forgot_password.html')


def logout_page(request):
    logout(request)
    return redirect('product_list')
    # return render(request, 'apps/auth/logout.html')


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'apps/product/product_grid.html', context)


def product_detail(request, pk=None):
    image = ProductImage.objects.filter(product_id=pk)
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
        'image': image
    }
    return render(request, 'apps/product/product_details.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            product = form.save()
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(image=image, product=product)

        return redirect('/')
    return render(request, 'apps/product/add_product.html')
