from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    event_date = models.DateTimeField()
    # Used a plural name for ManyToManyField since an event can have multiple attendees.
    # We don't need a separate model because we can directly connect it to the User model.
    # ManyToMany between two users (User <-> User) is usually not recommended,
    # but it's fine when linking users to other entities like events, groups, or projects.
    attendees  = models.ManyToManyField(User, related_name='events')

    def __str__(self):
        return self.title
