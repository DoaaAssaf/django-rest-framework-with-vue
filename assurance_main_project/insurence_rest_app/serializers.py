from rest_framework import serializers
from assurance_module_app.models import GeneralRisk, LandRisk
from rest_framework.fields import Field




class GeneralRiskSerializer(serializers.ModelSerializer):
 #   car_color = Field(default="red")

    class Meta:
        model = GeneralRisk
        fields = ("pk", "riskName","attr")



class LandRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRisk
        fields = ("pk", "riskName", "date", "address","zoneNumber", "space", "floorNumber",)
