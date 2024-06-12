from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.pk:  # If the object is new, set the customer_id to start from 8001
            last_customer = Customer.objects.order_by('-customer_id').first()
            self.customer_id = (last_customer.customer_id if last_customer else 8000) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
