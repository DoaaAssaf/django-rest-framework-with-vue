from django.conf.urls import include,url
from rest_framework import routers
from .viewsets import GeneralRiskViewSet,LandViewSet

router = routers.DefaultRouter() #default route to the rest api
router.register('insurance', GeneralRiskViewSet, "insurance")
router.register('lands', LandViewSet, "lands")
urlpatterns = [
    url(r'^', include(router.urls)),
]
