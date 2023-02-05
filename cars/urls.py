from django.urls import path

from cars.views import CarList, CreateSedan, CreateLorry, CreateGetOwner,GetCarTollArea


urlpatterns = [
    path('sedan/', CreateSedan.as_view()),
    path('lorry/', CreateLorry.as_view()),
    path('owner/', CreateGetOwner.as_view()),
    path('cars/', CarList.as_view()),
    path('cartollarea/', GetCarTollArea.as_view()),
]