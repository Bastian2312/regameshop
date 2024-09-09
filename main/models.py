from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name