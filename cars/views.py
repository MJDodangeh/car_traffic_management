from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from maps.views import CreateGraph
from violations.models import TrafficViolation
from .models import Owner, Car
from .serializers import OwnerSerializer, SedanSerializer, LorrySerializer, CarSerializer
from tolls.views import EditCarLocation_CreateToll
from tolls.models import TollStation


class CreateGetOwner(APIView):
    def post(self,request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        gte = request.GET.get('age__gte')
        lte = request.GET.get('age__lte')
        age = request.GET.getlist('age')
        try:
            if age:
                q = []
                for a in age:
                    q.extend(Owner.objects.filter(age=a))
            elif gte and lte:
                q = Owner.objects.filter(age__lte=lte,age__gte=gte)
            elif gte:
                q = Owner.objects.filter(age__gte=gte)
            elif lte:
                q = Owner.objects.filter(age__lte=lte)
            else:
                q=Owner.objects.all()
            res = OwnerSerializer(q,many=True)
            return Response(res.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CreateSedan(APIView):
    def post(self,request):
        serializer = SedanSerializer(data=request.data)
        if serializer.is_valid():
            s = serializer.save()
            EditCarLocation_CreateToll.addtoll(s.loc_edge, s.id)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateLorry(APIView):
    def post(self,request):
        serializer = LorrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["type"] = "lorry"
            s = serializer.save()
            if s.loc_edge.latitude <= 20:
                TrafficViolation.objects.create(car=s)
            EditCarLocation_CreateToll.addtoll(s.loc_edge,s.id)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CarList(APIView):
    def get(self,request):
        colors = request.GET.getlist('color')
        try:
            if colors:
                q = []
                for c in colors:
                    q.extend(Car.objects.filter(color=c))
            else:
                q=Car.objects.all()
            res = CarSerializer(q,many=True)
            return Response(res.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class GetCarTollArea(APIView):
    def get(self,request):
        try:
            tollstation_id = int(request.GET.get("tollstation"))
            area = int(request.GET.get("area"))
            cars = Car.objects.all()
            tsnodeid = TollStation.objects.get(id=tollstation_id).node.id
            res = []
            for car in cars:
                spath = CreateGraph.graph.shortestpath(car.loc_edge.to_node.id,
                                                       tsnodeid) + car.loc_nextnode_distance
                if spath <= area:
                    res.append({"car": car.id, "location_edge": car.loc_edge.id,
                                "location_distance_to_nextnode": car.loc_nextnode_distance, "distance_to_toll": spath})

            return Response({"cars": res}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)