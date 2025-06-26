from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from cart.models import Cart, CartItem
from myApp.models import Event
from .forms import CartAddForm



@login_required
def cart_add(request, pk):
    """Add ticket to cart."""
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    if request.method == "POST":
        form = CartAddForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart, _ = Cart.objects.get_or_create(user=user)

            # This Checks if the user has this item in his cart so doesnt duplicate it and just update the quantity
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=event,)
            if not created:
                cart_item.quantity += cd['quantity']
            else:
                cart_item.quantity = cd['quantity']

            cart_item.save()
            return redirect('cart:cart_list')
    else:
        form = CartAddForm()
    return render(request, "cart/cart_add.html", {"event": event, "form": form})


@login_required
def cart_list(request):
    cart = get_object_or_404(
        Cart.objects.prefetch_related('items__product'),
        user=request.user
    )
    return render(request, 'cart/cart_list.html', {'cart': cart})






