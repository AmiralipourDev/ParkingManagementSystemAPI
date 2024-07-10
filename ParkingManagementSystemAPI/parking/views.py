from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ParkingSpace, Reservation
from .serializers import ParkingSpaceSerializer, ReservationSerializer


class ParkingSpaceViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        available_spaces = ParkingSpace.objects.filter(is_occupied=False)
        serializer = self.get_serializer(available_spaces, many=True)
        return Response(serializer.data)
