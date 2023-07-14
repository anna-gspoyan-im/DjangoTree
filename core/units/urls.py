from django.urls import include, path
from rest_framework import routers
from .views import UnitsViewSet

router = routers.DefaultRouter()
router.register(r'units', UnitsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]