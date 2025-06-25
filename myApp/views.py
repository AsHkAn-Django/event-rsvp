from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Event
from .forms import EventForm
from cart.forms import CartAddForm
from cart.models import Cart, CartItem


class IndexView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = "myApp/index.html"




# @login_required
# def join_or_leave_event(request, pk):
#     event = get_object_or_404(Event, pk=pk)
#     user = request.user
#     if request.method == "POST":
#         if user in event.attendees.all():
#             event.attendees.remove(user)
#         else:
#             event.attendees.add(user)
#         return redirect('myApp:home')
#     return render(request, "myApp/join_and_leave_form.html", {"event": event, "form": EventForm()})


