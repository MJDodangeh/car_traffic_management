from django.core.exceptions import ValidationError
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
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)

class Sedan(Car):
    pass

class Lorry(Car):
    load_weight = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        if Lorry.objects.filter(owner_id=self.owner).exists():
            raise ValidationError('lorry for this owner exists')
        return super(Lorry, self).save(*args, **kwargs)