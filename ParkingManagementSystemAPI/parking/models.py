from django.db import models
from django.utils import timezone


# Create your models here.
class ParkingSpace(models.Model):
    space_number = models.CharField(max_length=10, unique=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return self.space_number


class Reservation(models.Model):
    parking_space = models.ForeignKey(to=ParkingSpace, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.parking_space.is_occupied = True
        self.parking_space.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.parking_space.space_number} reserved from {self.start_time} to {self.end_time}"
