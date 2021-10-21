from django.urls import path

from . import views

urlpatterns = [
    path('availability/<int:pk>/', views.Availability.as_view(), name='availability'),
    path('get-schedule/<int:pk>/', views.GetSchedule.as_view(), name='get_schedule'),
]
