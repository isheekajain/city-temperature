from django.db import models


# Create your models here.
CITY_CHOICES = (
    ('Mumbai', 'mumbai'),
    ('Delhi', 'delhi'),
    ('Chennai', 'chennai'),
    ('Bengaluru', 'bengaluru'),
    ('Kolkata', 'kolkata'),
)


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=10, choices=CITY_CHOICES, default='Mumbai')
    time = models.TimeField(auto_now_add=True, blank=True)