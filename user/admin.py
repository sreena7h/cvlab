from django.contrib import admin
from .models import User, AvailableTimeSlots

# Register your models here.

admin.site.register(User)
admin.site.register(AvailableTimeSlots)
