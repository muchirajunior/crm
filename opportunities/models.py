from django.db import models

from business_partners.models import BusinessPartner

class Opportunity(models.Model):
    STAGES = [
        ('qualification', 'Qualification'),
        ('proposal', 'Proposal'),
        ('negotiation', 'Negotiation'),
        ('closed_won', 'Closed Won'),
        ('closed_lost', 'Closed Lost'),
    ]

    name = models.CharField(max_length=255)
    stage = models.CharField(max_length=20, choices=STAGES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    close_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    business_partner = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)
    sales_person = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

