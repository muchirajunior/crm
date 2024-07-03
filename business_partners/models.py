from django.db import models

class BusinessPartner(models.Model):
    COMPANY_TYPES = [
        ('customer', 'Customer'),
        ('supplier', 'Supplier'),
        ('partner', 'Partner'),
    ]
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=COMPANY_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code
