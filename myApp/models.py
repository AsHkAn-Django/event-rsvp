from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    event_date = models.DateTimeField()

    def get_attendees(self):
        orders = self.order_items.filter(order__paid=True).select_related('order__user')
        return [item.order.get_display_name() for item in orders]

    def __str__(self):
        return self.title
