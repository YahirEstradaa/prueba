from django.db import models

class Customer(models.Model):
    CustomerId = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'Customers'
        managed = False         

    def __str__(self):
        return self.Name
