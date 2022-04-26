from operator import truediv
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, blank=False, primary_key=True, unique=True, verbose_name='User Name')
    password = models.CharField(max_length=255, blank=False, verbose_name='Account Password')
    phone = models.CharField(max_length=20, verbose_name='Phone Number')
    otp = models.CharField(max_length=6, verbose_name='OTP')
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
