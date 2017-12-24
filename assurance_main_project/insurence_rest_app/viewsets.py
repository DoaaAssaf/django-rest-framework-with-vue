from rest_framework import viewsets
from assurance_module_app.models import GeneralRisk, LandRisk
from .serializers import GeneralRiskSerializer,LandRiskSerializer


class GeneralRiskViewSet(viewsets.ModelViewSet):
    queryset = GeneralRisk.objects.all()
    serializer_class = GeneralRiskSerializer




class LandViewSet(viewsets.ModelViewSet):

    queryset =LandRisk.objects.all()
    serializer_class = LandRiskSerializer