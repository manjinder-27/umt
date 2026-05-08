from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Monitor
from .serializers import MonitorSerializer

@api_view(['GET'])
def list_monitors(request):
    if request.user.is_authenticated:
        try:
            monitors = Monitor.objects.filter(user=request.user)
            serializer = MonitorSerializer(monitors,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({'error':'Invalid Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'error':'Unauthorized Access'},status=status.HTTP_401_UNAUTHORIZED)
