from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core import serializers
from .serializers import ReservationSerializer
from .models import Reservation


# class ReservationViewSet(viewsets.ModelViewSet):
#     permissions_classes = [
#         permissions.IsAuthenticated,
#         #permissions.AllowAny,
#     ]
#     serializer_class = ReservationSerializer

#     def get_queryset(self):
#         return self.request.user.reservations.all()

class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_reservation=self.request.user)

    @action(methods=['get'], detail=False, url_path='user-reservations')
    def user_reservations(self, request):
        reservations = Reservation.objects.reservations_for_user(self.request.user)
        serializer = self.get_serializer(reservations, many=True)
        return Response(serializer.data)

    
   