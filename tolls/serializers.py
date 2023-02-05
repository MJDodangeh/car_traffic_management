from rest_framework.serializers import ModelSerializer

from tolls.models import TollStation, Toll


class TollStationSerializer(ModelSerializer):
    class Meta:
        model = TollStation
        fields = '__all__'

class TollSerializer(ModelSerializer):
    class Meta:
        model = Toll
        fields = '__all__'