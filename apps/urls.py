from django.urls import path
from apps.views import add_product, register, login_page, logout_page, forgot, product, product_details

urlpatterns = [
    path('', product, name='products'),
    path('product_details', product_details, name='product_details'),
    path('add_product', add_product, name='add_product'),
    path('register', register, name='register'),
    path('login', login_page, name='login'),
    path('logout', logout_page, name='logout'),
    path('forgot', forgot, name='forgot'),
]
