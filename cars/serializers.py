from rest_framework.serializers import ModelSerializer

from cars.models import Owner, Car, Sedan, Lorry


class OwnerSerializer(ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class SedanSerializer(ModelSerializer):
    class Meta:
        model = Sedan
        fields = '__all__'

class LorrySerializer(ModelSerializer):
    class Meta:
        model = Lorry
        fields = '__all__'




