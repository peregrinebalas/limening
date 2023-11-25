from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializers import AnimiSerializer
from .models import Animi

# Create your views here.
class AnimiShow(generics.RetrieveAPIView):

    def get(self, request, **kwargs):
        try:
            animi = Animi.objects.get(pk=kwargs['pk'])
            return Response(data= AnimiSerializer(animi).data, status=status.HTTP_200_OK)
        except (KeyError, Animi.DoesNotExist):
            return Response(data= {"error": "Could Not Find Animi"}, status=status.HTTP_404_NOT_FOUND)