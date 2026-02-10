from .models import Salom1, Salom2, Salom3, Salom4, Salom5
from .serializers import Salom1Serializers, Salom2Serializers, Salom3Serializers, Salom4Serializers,Salom5Serializers
from rest_framework.viewsets import ModelViewSet


class Salom1ModelViewSet(ModelViewSet):
    serializer_class = Salom1Serializers
    queryset = Salom1.objects.all()


class Salom2ModelViewSet(ModelViewSet):
    serializer_class = Salom2Serializers
    queryset = Salom2.objects.all()


class Salom3ModelViewSet(ModelViewSet):
    serializer_class = Salom3Serializers
    queryset = Salom3.objects.all()

class Salom4ModelViewSet(ModelViewSet):
    serializer_class = Salom4Serializers
    queryset = Salom4.objects.all()


class Salom5ModelViewSet(ModelViewSet):
    serializer_class = Salom5Serializers
    queryset = Salom5.objects.all()