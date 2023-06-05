from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NFhXCEibebLa5CBQPJgb95Z0YgWrPbRApuD0TTHTizvraUNds9Suj6rfABy5aBHisjFUg2s1XZfsBohJhmGpwJQ00phptzdEl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
