from rest_framework import serializers
from .models import City, Establishment

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True, source="establishment.name")
    title_id = serializers.PrimaryKeyRelatedField(queryset=Establishment.objects.all(), source="title")
    name = serializers.CharField(required=True, min_length=3)

    def validate_name(self, value):
        exist = Establishment.objects.filter(nombre__iexact=value).exists()

        if exist:
            raise serializers.ValidationError("This Establishment already exists")

        return value

    class Meta:
        model = Establishment
        fields = '__all__'
