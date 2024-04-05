from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
# Create your views here.
class FileApiView(ListCreateAPIView,RetrieveUpdateDestroyAPIView):
    queryset=Fileupload.objects.all()
    serializer_class=FileSerializer
    