from django.urls import path
from registration.views import Registration

urlpatterns = [
    path('registration/',Registration.as_view(),name='register')
]