from django.db import models
from phonenumber_field.modelfields import PhoneNumberField as PNF
from django.utils import timezone


# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)
    Phone = PNF()
    Address = models.CharField(max_length=300)
    Message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.Name


class Subscription(models.Model):
    SubEmail = models.EmailField(max_length=255)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.SubEmail
