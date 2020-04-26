from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from user.serializers import UserSerializer, PasswordSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
        Return the user specified by id.

        list:
        Return a list of all the existing users.

        create:
        Create a new user.

        update:
        Update of all user fields. Request should contain all user parameters.

        partial_update:
        Update of all or some of user fields. There is no requirement to contain all the parameters.

        delete:
        Delete the user specified by id.

    """
    queryset = User.objects.all()
    user_serializer = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_serializer_class(self):
        return self.user_serializer

    @action(methods=['post'], detail=True, url_path='change-password', url_name='change_password',
            permission_classes=[IsAuthenticated])
    def set_password(self, request, pk=None):
        """
        Change password via providing the old and new ones.
        """
        user = User.objects.get(id=pk)
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
