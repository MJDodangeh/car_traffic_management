from django.urls import path

from tolls.views import CreateTollStation, EditCarLocation_CreateToll, PayToll,TollList


urlpatterns = [
    path('tollstation/', CreateTollStation.as_view()),
    path('tolllist', TollList.as_view()),
    path('editcarlocation/<int:carid>/', EditCarLocation_CreateToll.as_view()),
    path('paytoll/', PayToll.as_view(),name="pay"),
]