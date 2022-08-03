from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Product

# Custom Decorators


def superuser_required(func):

    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry only store owners can do that.')
            return redirect(reverse('error_handler_500'))
        else:
            return func(request)

    return wrapper


# Product Views


def products(request):
    """ A view to handle all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)