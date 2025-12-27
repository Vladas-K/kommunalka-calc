from django.db import models

class MeterReading(models.Model):
    cold_prev = models.FloatField()
    cold_curr = models.FloatField()
    hot_prev = models.FloatField()
    hot_curr = models.FloatField()
    electricity = models.FloatField(default=0)
    internet = models.FloatField(default=0)

    cold_cost = models.FloatField()
    hot_cost = models.FloatField()
    sewage_cost = models.FloatField()
    total = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Платёж от {self.created_at.strftime('%Y-%m-%d %H:%M')}"
