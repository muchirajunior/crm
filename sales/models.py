from django.db import models

class SalesDocument(models.Model):
    number = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=100)
    customer_code = models.CharField(max_length=100)
    object_code = models.CharField(max_length=100)
    sales_employee = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number

class SalesDocumentItem(models.Model):
    document = models.ForeignKey(SalesDocument, on_delete=models.CASCADE)
    item_code = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.item_name} ({self.quantity})"

    def save(self, *args, **kwargs):
        if not self.number:
            last_document = SalesDocument.objects.order_by('-number').first()
            if last_document:
                last_number = int(last_document.number)
            else:
                last_number = 999  # Start from 1000 if no documents exist
            self.number = str(last_number + 1)
        super().save(*args, **kwargs)
