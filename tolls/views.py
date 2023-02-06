from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Car, Lorry,Sedan
from maps.models import Node, Edge
from maps.views import CreateGraph
from violations.models import TollViolation,TrafficViolation
from .models import TollStation, Toll
from .serializers import TollStationSerializer


class CreateTollStation(APIView):
    def post(self,request):
        locedge = request.data["edge"]
        locdis = int(request.data["nextnode_distance"])
        try:
            preedge = Edge.objects.get(id=locedge)
        except:
            return Response({"detail":"this edge does not exist"},status=status.HTTP_400_BAD_REQUEST)
        if locdis <= preedge.longitude:
            tlst = TollStation.objects.create(prevnode=preedge.from_node,nextnode=preedge.to_node,nextnode_distance=locdis)
            tlnode = Node.objects.create(name="toll"+str(tlst.id))
            tlst.node = tlnode
            tlst.save()
            leftedge = Edge.objects.create(from_node=preedge.from_node, to_node=tlnode ,name= preedge.from_node.name+"-"+tlnode.name,
                                           longitude=preedge.longitude-locdis ,latitude=preedge.latitude)
            rightedge = Edge.objects.create(from_node=tlnode, to_node=preedge.to_node ,name= tlnode.name+"-"+preedge.to_node.name,
                                            longitude=locdis ,latitude=preedge.latitude)
            EditCarLocation_CreateToll.editcarlocation(preedge,leftedge,rightedge,locdis)
            preedge.delete()
            CreateGraph.add_node_to_graph(leftedge.from_node,leftedge.to_node,leftedge.longitude)
            CreateGraph.add_node_to_graph(rightedge.from_node,rightedge.to_node,rightedge.longitude)
            res=TollStationSerializer(tlst)
            return Response(res.data,status=status.HTTP_201_CREATED)
        return Response({"detail":"distance is wrong"},status=status.HTTP_400_BAD_REQUEST)

class EditCarLocation_CreateToll(APIView):
    def put(self,request,carid):
        car = Car.objects.get(id=carid)
        locedge = request.data["loc_edge"]
        locdis = request.data["loc_nextnode_distance"]
        car.loc_edge_id = locedge
        car.loc_nextnode_distance = locdis
        car.save()
        l = Lorry.objects.filter(id=car.id)
        if l and car.loc_edge.latitude<=20:
            TrafficViolation.objects.create(car_id=car.id)

        res = self.addtoll(car.loc_edge,car.id)
        return Response(res, status=status.HTTP_202_ACCEPTED)

    @classmethod
    def addtoll(cls,locedge,carid):
        try:
            record = TollStation.objects.get(node=locedge.to_node)
            t = Toll.objects.create(toll_station=record,car_id= carid)
            l = Lorry.objects.filter(id=carid)
            if l:
                t.amount = t.amount + 300*l.first().load_weight
                t.save()
            return {"detail":"The following toll must be paid","car":t.car.id,"amount":t.amount}
        except:
            return {}

    @classmethod
    def editcarlocation(cls, deledge, leftnewedge, rightnewedge, distance):
        rec = Car.objects.filter(loc_edge=deledge)
        for r in rec:
            if r.loc_nextnode_distance <= distance:
                r.loc_edge = rightnewedge
                r.save()
            else:
                r.loc_edge = leftnewedge
                r.loc_nextnode_distance = r.loc_nextnode_distance - distance
                r.save()

class PayToll(APIView):
    def post(self,request):
        tollid = request.data["toll_id"]
        try:
            t = Toll.objects.get(id=tollid)
        except:
            return Response({"detail":"toll_id is wrong"},status=status.HTTP_400_BAD_REQUEST)
        if request.data["ispaid"]:
            t.ispaid = True
            t.save()
            return Response({"detail":"the toll was paid"},status=status.HTTP_202_ACCEPTED)
        else:
            TollViolation.objects.create(toll=t)
            return Response({"detail":"A toll violation occurred",
                             "car":t.car.id,"amount":t.amount},status=status.HTTP_200_OK)

class TollList(APIView):
    def get(self,request):
        try:
            starttime = request.GET.get('start_time')
            endtime = request.GET.get('end_time')
            car = request.GET.get('carid')
            owner = request.GET.get('ownerid')
            records = Toll.objects.filter(time__range=[starttime, endtime])
            if car:
                recs = records.filter(car_id=int(car))
                res = {"tolls": []}
                for r in recs:
                    i = {"tollstation": r.toll_station_id, "amount": r.amount, "time":r.time}
                    res["tolls"].append(i)
            elif owner:
                s = Sedan.objects.filter(owner_id = int(owner))
                l = Lorry.objects.filter(owner_id = int(owner))
                recs = records.filter(car__in=s)
                recl = records.filter(car__in=l)
                res = {"tolls": []}
                for rs in recs:
                    i = {"carid":rs.car_id,"tollstation": rs.toll_station_id, "amount": rs.amount, "time":rs.time}
                    res["tolls"].append(i)
                for rl in recl:
                    i = {"carid": rl.car_id, "tollstation": rl.toll_station_id, "amount": rl.amount, "time":rl.time}
                    res["tolls"].append(i)
            else:
                res = {"tolls": []}
                for r in records:
                    i = {"tollstation": r.toll_station_id, "amount": r.amount, "time": r.time}
                    res["tolls"].append(i)
            return Response(res, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
