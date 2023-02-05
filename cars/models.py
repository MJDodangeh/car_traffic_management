from django.db import models

from maps.models import Edge


class Owner(models.Model):
    name = models.CharField(max_length=32)
    national_code = models.CharField(max_length=32)
    age = models.IntegerField(default=0)

class Car(models.Model):
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    loc_edge = models.ForeignKey(Edge, on_delete=models.CASCADE,null=True)
    loc_nextnode_distance = models.IntegerField(default=0)
    Type_Choices = [('sedan', 'sedan'),('lorry', 'lorry')]
    type = models.CharField(max_length=5,choices=Type_Choices,default='sedan')

class Sedan(Car):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,null=True)

class Lorry(Car):
    owner = models.OneToOneField(Owner, on_delete = models.CASCADE,null=True)
    load_weight = models.IntegerField(default=0)