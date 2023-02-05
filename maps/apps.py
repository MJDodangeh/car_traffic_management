from django.apps import AppConfig

class MapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maps'
    def ready(self):
        from .models import Node,Edge
        from .graph import Graph
        from .views import CreateGraph
        node_list=[]
        edge_list=[]
        try:
            for node in Node.objects.all():
                node_list.append(node.id)
            for edge in Edge.objects.all():
                e = (edge.from_node.id,edge.to_node.id,edge.longitude)
                edge_list.append(e)
            G = Graph(edge_list, node_list)
            CreateGraph.graph = G
        except:
            G = Graph([], [])
            CreateGraph.graph = G



