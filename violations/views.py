from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from violations.models import TollViolation, TrafficViolation


class TollViolatorList(APIView):
    def get(self,request):
        tvls = TollViolation.objects.all()
        res = {"violators":[]}
        count = {}
        total_amount = {}
        for tv in tvls:
            ncode=tv.toll.car.owner.national_code
            i = {"name":tv.toll.car.owner.name,"nationalcode":ncode}
            if i not in res["violators"]:
                res["violators"].append(i)
                count[ncode] = 1
                total_amount[ncode] = tv.toll.amount
            else:
                count[ncode] += 1
                count[ncode] += tv.toll.amount
        for r in res["violators"]:
            r["count"] = count[r["nationalcode"]]
            r["total_amount"] = total_amount[r["nationalcode"]]
        res["violators"] = sorted(res["violators"],key=lambda x:x["total_amount"],reverse=True)
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