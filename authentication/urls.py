from .views import RegistrationView, UsernameValView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('register',RegistrationView.as_view(), name="register"),
    path('username-val',csrf_exempt(UsernameValView.as_view()), name="username-val"),
    
]