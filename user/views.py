from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_staff=False).order_by('username')

    def get(self, request, *args, **kwargs):
        """
            List users
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            create user details
            :param request: user details
            :param kwargs: NA
            :return: user details
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'data': serializer.data, 'message': 'Successfully created', 'status': status.HTTP_201_CREATED},
                status=status.HTTP_201_CREATED)
        return Response(
            {'status': status.HTTP_400_BAD_REQUEST, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class CreateInterviewer(generics.CreateAPIView):
    pass


class RemoveAccount(generics.DestroyAPIView):
    pass


class Availability(generics.RetrieveUpdateAPIView):
    pass
