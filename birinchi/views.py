from django.shortcuts import render
from .models import Salom1, Salom2, Salom3, Salom4, Salom5
from .serializers import Salom1Serializers, Salom2Serializers, Salom3Serializers, Salom4Serilizers, Salom5Serializers
from rest_framework.generics import ListCreateAPIView
# Create your views here.



class Salom1ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom1Serializers
    queryset = Salom1.objects.all()


class Salom2ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom2Serializers
    queryset = Salom2.objects.all()


class Salom3ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom3Serializers
    queryset = Salom3.objects.all()


class Salom4ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom4Serilizers
    queryset = Salom4.objects.all()


class Salom5ListCreateApiView(ListCreateAPIView):
    serializer_class = Salom5Serializers
    queryset = Salom5.objects.all()