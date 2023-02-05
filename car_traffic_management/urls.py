"""car_traffic_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from tolls.views import CreateTollStation, EditCarLocation_CreateToll, PayToll
from violations.views import TollViolatorList , TrafficViolationList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("maps.urls")),
    path('', include("cars.urls")),
    path('', include("tolls.urls")),
    path('violators/', TollViolatorList.as_view()),
    path('traffic/', TrafficViolationList.as_view())
]
