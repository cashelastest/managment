from django.urls import path
from .views import *

urlpatterns = [
path("user/<slug:profile_slug>/" , Home.as_view(), name = 'profile'),
path("sign-up/" , Registration.as_view(), name = 'sign_up'),
]