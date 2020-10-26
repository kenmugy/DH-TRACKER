from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=150)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    company = models.CharField(max_length=150)
    id_no = models.CharField(max_length=150, null=True)
    telephone = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)

