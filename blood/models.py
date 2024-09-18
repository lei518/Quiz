from django.conf import settings
from django.db import models


class BloodDonationRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('donating', 'Donating'),
        ('looking', 'Looking'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    blood_type = models.CharField(max_length=5)
    region = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    municipality = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_donation_date = models.DateField(null=True, blank=True)
