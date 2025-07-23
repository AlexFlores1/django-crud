from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=60,blank=False, null=False)
    last_name = models.CharField(max_length=60,blank=False, null=False)
    mobile = models.CharField(max_length=15,blank=False, null=False)
    phone = models.CharField(max_length=15,blank=True, null=True)
    email = models.EmailField(null=False, blank=False, default="no hay")
    company = models.CharField(max_length=20, blank=False, null=False)
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
