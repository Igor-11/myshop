from django.shortcuts import render

from .models import Product

from .utils.permission import login_required

@login_required
def home(request):
    products = Product.objects.all()
    context = {'user': request.session.get('user'), 'products': products}
    return render(request, 'shop/home.html', context)

def product_detail(request, product_id):
    return render(request, 'shop/product_detail.html')
