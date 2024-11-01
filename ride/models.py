from django.db import models
from django.contrib.auth.models import User,Group


class Driver(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("not_available", "Not Available"),
        ("way_to_pickup", "Way to Pick Up"),
        ("reached_pickup", "Reached Pickup"),
        ("way_to_dropoff", "Way to Drop Off"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name= 'group')
    phone_no = models.CharField(max_length=15)
    nid_no = models.CharField(max_length=100,null= True,blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available",
    )
    latitude = models.CharField(max_length=100,null= True,blank=True)
    longitude = models.CharField(max_length=100,null=True,blank= True)
