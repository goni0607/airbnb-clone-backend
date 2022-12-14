from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Check-in date is in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("Check-out date is in the past!")
        return value

    def validate(self, attrs):
        if attrs['check_out'] <= attrs['check_in']:
            raise serializers.ValidationError(
                "Check-in date must be earlier than check-out date.")
        if Booking.objects.filter(
            room=self.context['room'],
            check_in__lte=attrs['check_out'],
            check_out__gte=attrs['check_in'],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return attrs


class PublicBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
