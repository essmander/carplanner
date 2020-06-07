from rest_framework import serializers
from .models import Reservation
from datetime import date
from django.db.models import Q


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        
        df = data['date_from']
        dt = data['date_to']

        if df < date.today():
            raise serializers.ValidationError("You can not make an reservation in the past")
        if dt < date.today():
            raise serializers.ValidationError("You can not make an reservation in the past")
        if df > dt:
            raise serializers.ValidationError("Date from can not be higer than date to")
        
        startTime = data['start_time']        
        endTime = data['end_time']        

        if df == dt and startTime == endTime:
            raise serializers.ValidationError("You are not making any reservation data from and data to is the same. So is start time and end time")

        #         #dates
        if Reservation.objects.filter(Q(date_from__lt=df) & Q(date_to__gt=df)).exists():
            raise serializers.ValidationError("FIRST IF for date")

        if Reservation.objects.filter(Q(date_from__lt=dt) & Q(date_to__gt=dt)).exists():
            raise serializers.ValidationError("2 IF for date")

        if Reservation.objects.filter(Q(date_from__gt=df) & Q(date_to__lt=dt)).exists():
            raise serializers.ValidationError("3 IF for date")

        #time
        if Reservation.objects.filter(Q(date_from__exact=df) & Q(start_time__lte=startTime)).exists():
            raise serializers.ValidationError("FIRST IF")

        if Reservation.objects.filter(Q(date_from__exact=df) & Q(end_time__gte=startTime)).exists():
            raise serializers.ValidationError("SECOND IF Ther is already an reservation")

        if Reservation.objects.filter(Q(date_from__exact=dt) & Q(start_time__gt=endTime)).exists():
           raise serializers.ValidationError("3 IF :Ther is already an reservation")

        if Reservation.objects.filter(Q(date_from__exact=df) & Q(end_time__gte=startTime)).exists():
            raise serializers.ValidationError("4 IF. Ther is already an reservation")

        return data