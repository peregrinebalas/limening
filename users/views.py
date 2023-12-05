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
        try:
            user = UserSerializer(data=request.data, context={'request': request}, partial=True)
            print(user.is_valid())
            if user.is_valid():
                user.save()
                return Response(user.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={
                "error": "Fields missing, could not create user."
                }, status=status.HTTP_400_BAD_REQUEST)
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
        try:
            user = User.objects.get(pk=kwargs['pk'])
            serializer = UserSerializer(user, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data={
                "error": "Fields missing, could not create user."
                }, status=status.HTTP_400_BAD_REQUEST)
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