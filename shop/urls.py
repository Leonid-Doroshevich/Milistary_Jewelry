from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<slug:slug>', views.product, name='product'),
    path('cart/add/<int:product_id>', views.basket_add, name='basket_add'),
    path('cart/remove/<int:basket_id>', views.basket_remove, name='basket_remove'),
    
]
