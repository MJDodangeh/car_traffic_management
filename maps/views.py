from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Node
from .serializers import EdgeSerializer
from .graph import Graph


class CreateGraph(APIView):
    graph = Graph([], [])
    @classmethod
    def add_node_to_graph(cls,fromnode, tonode, longitude):
        if fromnode.id not in cls.graph.node_list:
            cls.graph.node_list.append(fromnode.id)
            cls.graph.adjacency_list.update({fromnode.id: []})
        if tonode.id not in cls.graph.node_list:
            cls.graph.node_list.append(tonode.id)
            cls.graph.adjacency_list.update({tonode.id: []})
        newedge = (fromnode.id, tonode.id, int(longitude))
        cls.graph.edge_list.append(newedge)
        cls.graph.adjacency_list[fromnode.id].append((tonode.id,int(longitude)))

    def post(self,request):
        from_node = request.data["fromnode"]
        to_node = request.data["tonode"]
        fromnode = Node.objects.filter(name=from_node).first()
        tonode = Node.objects.filter(name=to_node).first()
        if not fromnode:
            fromnode = Node.objects.create(name=from_node)
        if not tonode:
            tonode = Node.objects.create(name=to_node)
        if fromnode==tonode:
            return Response({"detail":"fromnode and tonode cannot be the same"},status=status.HTTP_400_BAD_REQUEST)
        serializer = EdgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data["from_node"]=fromnode
            serializer.validated_data["to_node"]=tonode
            serializer.save()
            CreateGraph.add_node_to_graph(fromnode,tonode,request.data["longitude"])
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        return Response(CreateGraph.graph.adjacency_list ,status=status.HTTP_200_OK)




