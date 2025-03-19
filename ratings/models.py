from django.db import models


class Rating(models.Model):
    beer_name = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=1)
    notes = models.TextField(blank=True)
    brewer = models.TextField(blank=True)
