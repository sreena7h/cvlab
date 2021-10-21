from django.db import models

# Create your models here.
from user.models import User


class AvailableTimeSlots(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    objects = models.Manager()

    class Meta:
        unique_together = ('user', 'from_time', 'to_time')


class Interview(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(AvailableTimeSlots, on_delete=models.SET_NULL, null=True, blank=True)
    created_time = models.DateTimeField('date created', auto_now_add=True)
    updated_time = models.DateTimeField('date updated', auto_now=True)

    objects = models.Manager()
