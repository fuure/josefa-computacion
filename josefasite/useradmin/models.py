from django.db import models

class Meta():
    managed = True

class Customer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    