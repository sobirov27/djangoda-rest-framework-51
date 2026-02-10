from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('birinchi/', include('birinchi.urls')),
    path('ikkinchi/', include('ikkinchi.urls')),
    path('uchinchi/', include('uchinchi.urls')),
    path('tortinchi/', include('tortinchi.urls')),
]
