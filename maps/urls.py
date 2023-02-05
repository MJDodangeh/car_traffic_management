from django.urls import path

from .views import CreateGraph


urlpatterns = [
    path('map/', CreateGraph.as_view())
]