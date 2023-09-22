from django import forms
from .models import Reports
from packages.models import Bookings
from person.models import Person



class RepostForm(forms.ModelForm):
    
    class Meta:
        model = Reports
        fields = ['User','Booking','ReportType','StartDate','EndDate','ReportData']
    
    User = forms.ModelChoiceField(queryset=Person.objects.all(),  label='User',widget = forms.Select(attrs={'class': 'form-control', 'placeholder': 'User'}))
    Booking = forms.ModelChoiceField(queryset=Bookings.objects.all(), label='Booking',widget = forms.Select(attrs={'class': 'form-control', 'placeholder': 'Booking'}))
    REPORT_CHOICES = (
        ('User', 'User'), ('Booking', 'Booking')
    )
    ReportType = forms.ChoiceField(label='Report Type',choices=REPORT_CHOICES,widget = forms.Select(attrs={'class': 'form-control', 'placeholder': 'Report Type'}),)
    StartDate = forms.DateField(label='Start Date',widget = forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Start Date','type':'date'}))
    EndDate = forms.DateField(label='End Date',widget = forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'End Date','type':'date'}),)
    ReportData = forms.CharField(label='Report Data',max_length=250, widget = forms.Textarea(attrs={ 'class': 'form-control', 'placeholder': 'Report Data','rows':5,}))
    
    
    
    