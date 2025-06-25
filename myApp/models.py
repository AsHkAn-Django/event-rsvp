from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    event_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_attendees(self):
        orders = self.order_items.filter(order__paid=True).select_related('order__user')
        return [item.order.get_display_name() for item in orders]

    def __str__(self):
        return self.title
