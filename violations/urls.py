from django.urls import path, include
from .views import TollViolatorList , TrafficViolationList


urlpatterns = [
    path('tollviolators', TollViolatorList.as_view()),
    path('trafficviolations', TrafficViolationList.as_view())
]