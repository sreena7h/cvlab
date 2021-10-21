from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True, null=False, blank=False)
    # is staff can be used for interviewer

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class AvailableTimeSlots(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'from_time', 'to_time')

