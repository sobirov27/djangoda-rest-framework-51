from django.urls import path, include
from .views import Salom1ModelViewSet, Salom2ModelViewSet, Salom3ModelViewSet, Salom4ModelViewSet, Salom5ModelViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()

r.register(r'salom1', Salom1ModelViewSet)

urlpatterns = [
    path('', include(r.urls)),
]


r.register(r'salom2', Salom2ModelViewSet)

urlpatterns = [
    path('', include(r.urls)),
]


r.register(r'salom3', Salom3ModelViewSet)

urlpatterns = [
    path('', include(r.urls)),
]


r.register(r'salom4', Salom4ModelViewSet)

urlpatterns = [
    path('', include(r.urls)),
]


r.register(r'salom5', Salom5ModelViewSet)

urlpatterns = [
    path('', include(r.urls)),
]