from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import AvailableTimeSlots, Interview
from .utils import is_time_between


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTimeSlots
        fields = ['user', 'from_time', 'to_time']

    def validate(self, attrs):
        if attrs['from_time'] >= attrs['to_time']:
            raise ValidationError('Invalid format: From time > To time.')

        current_slots = AvailableTimeSlots.objects.filter(user=attrs['user'])
        for slot in current_slots:
            if is_time_between(slot.from_time, slot.to_time, attrs['from_time']) or \
                    is_time_between(slot.from_time, slot.to_time, attrs['to_time']):
                raise ValidationError('Provided timeslot is already taken.')
        return attrs

    def create(self, validated_data):
        obj = AvailableTimeSlots(**validated_data)
        obj.save()
        return obj


class GetScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['user', 'schedule']

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        obj = Interview(**validated_data)
        obj.save()
        return obj
