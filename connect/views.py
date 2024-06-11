from django.shortcuts import render
from .models import message
from .serializers import MessageSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class MessageViewSet(ModelViewSet):
    queryset = message.objects.all()
    serializer_class = MessageSerializer


