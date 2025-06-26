from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import OrderItem
from cart.models import CartItem


def order_create(request):
    cart_items = CartItem.objects.filter(cart__user = request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )
            return redirect('payment:process')
    else:
        form = OrderForm()
    return render(request, 'order/order_create.html', {'form': form})

