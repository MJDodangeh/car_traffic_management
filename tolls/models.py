from django.db import models

from cars.models import Car
from maps.models import Edge, Node


class TollStation(models.Model):
    prevnode = models.ForeignKey(Node, on_delete=models.CASCADE,related_name="prev", null=True)
    nextnode = models.ForeignKey(Node, on_delete=models.CASCADE,related_name='next', null=True)
    nextnode_distance = models.IntegerField(default=0)
    node = models.OneToOneField(Node, on_delete=models.CASCADE, null=True)

class Toll(models.Model):
    toll_station = models.ForeignKey(TollStation, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    amount = models.IntegerField(default=5000)
    time = models.DateTimeField(auto_now_add=True)
    ispaid = models.BooleanField(default=False)

