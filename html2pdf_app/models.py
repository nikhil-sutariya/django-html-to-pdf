from django.db import models

class Bill(models.Model):
    bill_no = models.CharField(max_length=150)
    customer_name = models.CharField(max_length=100)
    cosutmer_phone = models.IntegerField()
    product_name = models.CharField(max_length=500)
    amount = models.IntegerField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.customer_name.capitalize()

    class Meta:
        ordering = ('date',)