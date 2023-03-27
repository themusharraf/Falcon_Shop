from django.urls import path
from apps.views import add_product, register, login_page, logout_page, forgot, product_list, product_detail

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('add_product', add_product, name='add_product'),
    path('register', register, name='register'),
    path('login', login_page, name='login_page'),
    path('logout', logout_page, name='logout_page'),
    path('forgot', forgot, name='forgot'),
]
