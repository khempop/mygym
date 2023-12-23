from gym.models import *
from gym.serializers import GymSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GymView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Gym.objects.get(pk=pk)
        except Gym.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        gym = self.get_object(id)
        serializer = GymSerializer(gym)
        return Response(serializer.data)

    def put(self, request, format=None):
        id = request.data['id']
        gym = self.get_object(id)
        serializer = GymSerializer(gym, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        id = request.data['id']
        gym = self.get_object(id)
        gym.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GymList(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Gym.objects.get(pk=pk)
        except Gym.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        serializer = GymSerializer()
        return Response(serializer.data)