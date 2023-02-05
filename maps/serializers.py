from rest_framework.serializers import ModelSerializer

from .models import Node, Edge


class EdgeSerializer(ModelSerializer):
    class Meta:
        model = Edge
        fields = '__all__'

class NodeSerializer(ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'