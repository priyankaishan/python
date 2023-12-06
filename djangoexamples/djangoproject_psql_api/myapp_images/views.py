# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Product
import base64


def shop_home(request):
    return render(request, 'temp_myapp_images/shop_home.html')



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.image_data_bytea = form.cleaned_data['image'].read()
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'temp_myapp_images/add_product.html', {'form': form})



def product_list(request):
    products = Product.objects.all()
    return render(request, 'temp_myapp_images/product_list.html', {'products': products})