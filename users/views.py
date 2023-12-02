from django.contrib.auth.models import User
# from rest_framework import permissions, viewsets

from django.db.utils import IntegrityError

from rest_framework import generics, permissions
# from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import status

from users.serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

class CreateUser(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        # first_name = request.data.get("first_name", None)
        # last_name = request.data.get("last_name", None)
        user = User.objects.create_user(username, password, email)
        data = UserSerializer(instance=user, context={'request': request}).data
        try:
            # user = User.objects.create_user(username, password, email)
            return Response(data=data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(data={
                "error": "Fields missing, could not create user."
            }, status=status.HTTP_409_CONFLICT)
        except TypeError:
            return Response(data={
                "error": "Fields missing, could not create user."
            }, status=status.HTTP_409_CONFLICT)

class UpdateUser(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    def patch(self, request, *args, **kwargs):
        username = request.data.get("username", None)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        try:
            user = User.objects.get(pk=kwargs['pk'])
            user.username=username
            user.password=password
            user.email=email
            user.first_name=first_name
            user.last_name=last_name
            user.save

            return Response(data=UserSerializer(user).data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)
        except TypeError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)
        
class DeleteUser(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['pk'])
            user.delete

            return Response(data=UserSerializer(user).data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)
        except TypeError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)
        
class ShowUser(generics.UpdateAPIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(pk=kwargs['pk'])
            data = UserSerializer(instance=user, context={'request': request}).data
            print(data)
            return Response(data=data, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)
        except TypeError:
            return Response(data={
                "error": "Fields missing, could not save user."
            }, status=status.HTTP_409_CONFLICT)