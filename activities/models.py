from django.db import models

from business_partners.models import BusinessPartner
from sales.models import SalesDocument

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('phone_call', 'Phone Call'),
        ('visit', 'Visit'),
        ('campaign', 'Campaign'),
        ('meeting', 'Meeting'),
        ('other', 'Other'),
    ]

    sales_person_name = models.CharField(max_length=100)
    business_partner = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)
    sales_document = models.ForeignKey(SalesDocument, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sales_person_name} - on {self.date}"
