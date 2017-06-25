from django.shortcuts import render
from .forms import SubcriberForm
from products.models import *

# Create your views here.
def landing(request):
    form = SubcriberForm(request.POST or None)
    if request.POST and form.is_valid():
        print(request.POST)
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()
    return render(request, 'landing/landing.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category = 2)
    products_images_laptops = products_images.filter(product__category = 1)
    return render(request, 'landing/home.html', locals())