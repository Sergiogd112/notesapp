from django.urls import path

from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name='register'),
    path('login/', UserRegistrationView.as_view(),name='login'),

]
