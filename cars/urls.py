from django.urls import path

from cars.views import CarList, CreateSedan, CreateLorry,GetCarTollArea,CreateOwner ,OwnersCarList


urlpatterns = [
    path('sedan/', CreateSedan.as_view()),
    path('lorry/', CreateLorry.as_view()),
    path('owner/', CreateOwner.as_view()),
    path('cars', CarList.as_view()),
    path('cartollarea', GetCarTollArea.as_view()),
    path('ownerscar', OwnersCarList.as_view()),
]