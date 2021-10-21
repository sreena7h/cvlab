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


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['candidate', 'interviewer', 'slot']

    def validate(self, attrs):
        Interview.objects.filter(candidate=attrs['user']).update(slot=None)
        slots = AvailableTimeSlots.objects.filter(user=attrs['user']).order_by('from_time')

        if slots.filter(user__is_staff=True):
            raise ValidationError('Only candidates can request for schedule')

        if not slots:
            raise ValidationError('Please pick some available time slots')

        interviewer_slots = AvailableTimeSlots.objects.filter(user__is_staff=True, picked_status=False)

        flag = False
        for slot in slots:
            possible_schedules = interviewer_slots.filter(from_time__gte=slot.from_time,
                                                          to_time__lte=slot.to_time).order_by('from_time')
            if possible_schedules:
                flag = True
                attrs['slot'] = slot
                AvailableTimeSlots.objects.filter(pk=attrs['slot']).update(picked_status=True)
                AvailableTimeSlots.objects.filter(pk=possible_schedules[0]).update(picked_status=True)
                attrs['interviewer'] = possible_schedules[0].id
                break

        if not flag:
            raise ValidationError('No schedules available, Add or update time slots')

        return attrs

    def create(self, validated_data):
        obj = Interview.objects.get_or_create(candidate=validated_data['user'])
        obj.interviewer = validated_data['interviewer']
        obj.slot = validated_data['slot']
        obj.save()
        return obj
