from django.db import models

class Bin(models.Model):
    location = models.CharField(max_length=100)
    
    fill_level = models.IntegerField()   # 0–100 %
    capacity = models.IntegerField(default=100)

    # Coordinates for mapping
    x = models.FloatField()
    y = models.FloatField()

    # Optional: last updated time (good for future)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location