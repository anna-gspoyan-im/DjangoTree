from rest_framework import viewsets
from .models import Units
from .serializers import UnitsSerializer


class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
