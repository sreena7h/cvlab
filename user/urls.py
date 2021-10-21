from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('list-users/', views.ListUsers.as_view(), name='list_users'),
    path('add-interviewer/', views.CreateInterviewer.as_view(), name='add_interviewer'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
