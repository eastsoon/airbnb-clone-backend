from django.utils import timezone
from rest_framework import serializers
from .models import Booking


class CreateBookingSerializer(serializers.ModelSerializer):

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
            raise serializers.ValidationError("잘못된 날짜 입니다.")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        if now > value:
            raise serializers.ValidationError("잘못된 날짜 입니다.")
        return value

    def validate(self, data):
        if data["check_in"] >= data["check_out"]:
            raise serializers.ValidationError("체크아웃 날짜를 확인해주세요.")

        if Booking.objects.filter(
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError("이미 예약된 객실이 있습니다.")
        return data


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "kind",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )
