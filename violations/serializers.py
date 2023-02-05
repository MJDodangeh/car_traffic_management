from rest_framework.serializers import ModelSerializer
from violations.models import TollViolation,TrafficViolation


class TollViolationSerializer(ModelSerializer):
    class Meta:
        model = TollViolation
        fields = '__all__'

class TrafficViolationSerializer(ModelSerializer):
    class Meta:
        model = TrafficViolation
        fields = '__all__'