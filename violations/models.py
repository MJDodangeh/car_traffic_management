from datetime import datetime

from django.db import models
from django.utils import timezone

from cars.models import Car, Lorry


class TollViolation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class TrafficViolation(models.Model):
    car = models.ForeignKey(Lorry, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)