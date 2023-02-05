from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=32,null=True)

    def __str__(self):
        return self.name

class Edge(models.Model):
    from_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='fromnode', null=True)
    to_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='tonode', null=True)
    longitude = models.IntegerField(default=0) #طول
    latitude = models.IntegerField(default=0) #عرض
    name = models.CharField(max_length=32,null=True)

    def __str__(self):
        return self.name

