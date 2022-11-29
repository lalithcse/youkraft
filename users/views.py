from .models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'list']

    def list(self, request):
        """
        To list all data of users
        HTTP method : get
        :param request: request object
        :return: Response
        """
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Retrieve pk's user id info
        :param request: request object
        :param pk: user id
        :return: Response
        """
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Creates a new user
        :param request: request object
        :param args: arguments
        :param kwargs: kwargs
        :return: Response
        """
        user = request.user
        data = {
            "username": request.POST.get('username', None),
            "password": request.POST.get('password', None),
            "email": request.POST.get('email', None),
        }
        serializer = self.serializer_class(data=data,  # or request.data
                                           context={'author': user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        """
        Updates the existing user. overwrites the update method.
        :param request: request object
        :param pk: user id
        :param args: arguments
        :param kwargs: kwargs
        :return: Response
        """
        return super().update(request, pk, *args, **kwargs)

    def destroy(self, request, pk=None, *args, **kwargs):
        """
        Destroys the existing user
        :param request: request object
        :param pk: user id
        :param args: arguments
        :param kwargs: kwargs
        :return: Response
        """
        return super().destroy(request, pk, *args, **kwargs)


class AuthViewset(viewsets.ViewSet):
    """
    Authenticate api to just check the password of existing user
    """
    def create(self, request):
        """
        POST request to auth
        :param request:
        :return:
        """
        username = request.data.get('username')
        password = request.data.get('password')
        # get the user from the request
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            return Response("Passwords match",
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("Passwords do not match",
                            status=status.HTTP_400_BAD_REQUEST)
