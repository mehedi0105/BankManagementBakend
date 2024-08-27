from django.db import models
from django.contrib.auth.models import User
from .constraints import ACCAUNT_TYPE, GENDER

# Create your models here.

class UserAccount (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images/')
    account_type = models.CharField(max_length=100, choices=ACCAUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    street_address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username