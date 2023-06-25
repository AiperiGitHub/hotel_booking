from email.policy import default

from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    user = serializers.IntegerField()
    room = serializers.IntegerField()
    checkin_date = serializers.DateField()
    checkout_date = serializers.DateField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'checkin_date', 'checkout_date', ]


