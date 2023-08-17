from rest_framework import serializers
from .models import SchoolFacility, Laboratory


class SchoolFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFacility
        fields = "__all__"


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = "__all__"
