from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import AvailableTimeSlots, Interview
from .serializers import AvailabilitySerializer, ScheduleSerializer


class Availability(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
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


class Schedule(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = Interview.objects.filter(candidate_id=self.kwargs.get('pk'))
        return queryset

    def get(self, request, *args, **kwargs):
        """ Get the scheduled time """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Create Schedule for interview """
        data = request.data
        data['user'] = self.kwargs.get('pk')
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(dict(data=serializer.data, status=status.HTTP_201_CREATED), status=status.HTTP_201_CREATED)
        else:
            return Response(dict(status=status.HTTP_400_BAD_REQUEST, errors=serializer.errors),
                            status=status.HTTP_400_BAD_REQUEST)

    # todo: update and delte
