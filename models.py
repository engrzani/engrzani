from django.db import models
from person.models import Person
from packages.models import Bookings

# Create your models here.


class Reports(models.Model):
    User = models.ForeignKey(Person,on_delete=models.CASCADE)
    Booking = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    REPORT_CHOICES = (
        ('User', 'User'), ('Booking', 'Booking')
    )
    ReportType = models.CharField(max_length=10,choices=REPORT_CHOICES)
    StartDate = models.DateField()
    EndDate = models.DateField()
    ReportData = models.CharField(max_length=250)
    CreatedAt = models.DateField(auto_now_add=True)