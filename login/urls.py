from unicodedata import name
from django.urls import path

from . views import *

urlpatterns = [
    path('', home, name='Home'),
    path('otp', otp, name='OTP'),
    path('message', message, name='Message')
]
