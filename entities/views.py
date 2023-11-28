from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import EntitySerializer
from .models import Entity

# Create your views here.
class EntityShow(generics.RetrieveAPIView):

    def get(self, request, **kwargs):
        try:
            entity = Entity.objects.get(pk=kwargs['pk'])
            return Response(data= EntitySerializer(entity).data, status=status.HTTP_200_OK)
        except (KeyError, Entity.DoesNotExist):
            return Response(data= {"error": "Could Not Find Entity"}, status=status.HTTP_404_NOT_FOUND)