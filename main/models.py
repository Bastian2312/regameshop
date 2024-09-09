from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.mood_intensity > 5