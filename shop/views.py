from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Category, Product, Basket
from users.models import User
from .forms import Quantity
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    return render(request, 'shop/index.html')

def catalog(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/catalog.html', {'products': products})

def product(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    images = [product.image1, product.image2, product.image3, product.image4, product.image5, product.image6, product.image7, product.image8]
    if request.method == 'POST':
        if request.user.is_authenticated:
            baskets = Basket.objects.filter(user=request.user, product=product)
            form = Quantity(data=request.POST)
            product_id = product.id
            print(product_id)
            if form.is_valid():
                quantity = request.POST['quantity']
                if not baskets.exists():
                    Basket.objects.create(user=request.user, product=product, quantity=quantity)
                else:
                    basket = baskets.first()
                    basket.quantity += int(quantity)
                    basket.save()
                messages.success(request, 'Product added to cart!')
                return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.success(request, 'You must to login first!')
            return HttpResponseRedirect(reverse('users:login'))         
    else:
        form = Quantity()
   
    
    context = {'product': product, 'images': images, 'form': form}
    return render(request, 'shop/product.html', context)

@login_required
def basket_add(request, product_id, quantity = 1):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += quantity
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER']) 

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])