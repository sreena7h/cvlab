from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import AvailableTimeSlots
from .serializers import AvailabilitySerializer


class Availability(generics.ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        queryset = AvailableTimeSlots.objects.filter(user_id=self.kwargs.get('pk')).order_by('-from_time', '-to_time')
        return queryset

    def get(self, request, *args, **kwargs):
        """ List Availability of Examiners or Candidates """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = request.data
        data['user'] = self.kwargs.get('pk')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(data=serializer.data, status=status.HTTP_201_CREATED), status=status.HTTP_201_CREATED)
        else:
            return Response(dict(status=status.HTTP_400_BAD_REQUEST, errors=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)


class GetSchedule(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AvailabilitySerializer

    def get_queryset(self):
        queryset = AvailableTimeSlots.objects.filter(user_id=self.kwargs.get('pk')).order_by('-from_time', '-to_time')
        return queryset

    def create(self, request, *args, **kwargs):
        """ List Availability of Examiners or Candidates """
        return self.create(request, *args, **kwargs)


class UpdateSchedule(generics.RetrieveUpdateDestroyAPIView):
    pass
