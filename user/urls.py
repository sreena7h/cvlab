from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListCreate.as_view(), name='user_list_create'),
    path('add-interviewer', views.CreateInterviewer.as_view(), name='add_interviewer'),
    path('delete-user/<int:pk>/', views.RemoveAccount.as_view(), name='book_detail_view'),
    path('get-availability/<int:pk>/', views.Availability.as_view(), name='availability')
]
