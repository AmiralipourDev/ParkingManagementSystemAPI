from rest_framework import serializers
from .models import ParkingSpace, Reservation


class ParkingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpace
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        parking_space = data.get("parking_space")
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if Reservation.objects.filter(parking_space=parking_space, start_time__lt=end_time,
                                      end_time__gt=start_time).exists():
            raise serializers.ValidationError("This parking space is already reserved for the specified time.")

        return data

    def create(self, validated_data):
        reservation = super().create(validated_data)
        reservation.parking_space.is_occupied = True
        reservation.parking_space.save()
        return reservation
