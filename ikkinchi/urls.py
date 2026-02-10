from django.urls import path
from .views import Salom1ListCreateApiView, Salom2ListCreateApiView, Salom3ListCreateApiView, Salom4ListCreateApiView, Salom5ListCreateApiView



urlpatterns = [
    path('salom1/', Salom1ListCreateApiView.as_view()),
    path('salom2/', Salom2ListCreateApiView.as_view()),
    path('salom3/', Salom3ListCreateApiView.as_view()),
    path('salom4/', Salom4ListCreateApiView.as_view()),
    path('salom5/', Salom5ListCreateApiView.as_view()), 
]