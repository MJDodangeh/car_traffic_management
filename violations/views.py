from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from violations.models import TollViolation, TrafficViolation


class TollViolatorList(APIView):
    def get(self,request):
        tvls = TollViolation.objects.all()
        res = {"violators":[]}
        count = {}
        for tv in tvls:
            i = {"name":tv.car.owner.name,"nationalcode":tv.car.owner.national_code}
            if i not in res["violators"]:
                res["violators"].append(i)
                count[tv.car.owner.national_code] = 1
            else:
                count[tv.car.owner.national_code] += 1
        for r in res["violators"]:
            r["count"] = count[r["nationalcode"]]
        return Response(res, status=status.HTTP_202_ACCEPTED)

class TrafficViolationList(APIView):
    def get(self,request):
        vls = TrafficViolation.objects.all()
        res = {"cars":[]}
        count = {}
        for v in vls:
            i = {"id":v.car.id,"owner":v.car.owner.id}
            if i not in res["cars"]:
                res["cars"].append(i)
                count[v.car.id] = 1
            else:
                count[v.car.id] += 1
        for r in res["cars"]:
            r["count"] = count[r["id"]]
        return Response(res, status=status.HTTP_202_ACCEPTED)