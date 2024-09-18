from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    weight = models.FloatField()
    height = models.FloatField()
    region = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=3)
    availability = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True)
