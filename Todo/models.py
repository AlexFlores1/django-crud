from django.db import models
from datetime import date

class Todo(models.Model):
    title = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    endtime = models.DateField(null=True)
    priority = models.IntegerField(default=3)
    def __str__(self):
        return self.title
# Create your models here.
