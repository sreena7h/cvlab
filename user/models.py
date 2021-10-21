from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True, null=False, blank=False)
    # is staff can be used for interviewer

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

