import stripe
from django.shortcuts import render, Http404
from .models import Product
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def product_view(request):
    product = Product.objects.all()
    return render(request, 'product.html', {'product': product})


def payment_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        raise Http404('entered product does not exists!!!')
    return render(request, 'payment.html', {'product': product, 'key': settings.STRIPE_PUBLISHABLE_KEY})


def success_view(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='Payment for product',
            source=request.POST['stripeToken']
        )
        return render(request, 'success.html', {'charge': charge})
    else:
        return render(request, 'success.html')
    return render(request, 'success.html')



