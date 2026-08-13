from django.db import models
from django.db import models


class Trail(models.Model):

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("hard", "Hard"),
        ("expert", "Expert"),
    ]

    name = models.CharField(max_length=100)

    distance_km = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    elevation_gain = models.IntegerField()

    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES
    )

    is_open = models.BooleanField(default=True)

    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def distance(self):
        return self.distance_km

    @property
    def elevation(self):
        return self.elevation_gain
    
