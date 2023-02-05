from queue import PriorityQueue

class Graph():
    def __init__(self, edge_list, node_list):
        self.adjacency_list = {node:[] for node in node_list}
        self.edge_list=edge_list
        self.node_list=node_list
        self.node_degree_list = dict()
        self.node_parent_list = dict()

        for e in edge_list:
            self.adjacency_list[e[0]].append((e[1],e[2]))

    def initialize(self,source):
        for node in self.node_list:
            self.node_degree_list[node] = float('inf')
            self.node_parent_list[node] = None
        self.node_degree_list[source]=0

    def w(self,u,v):
        for e in self.adjacency_list[u]:
            if e[0] == v:
                return e[1]
        return None

    def relax(self,u,v):
        w = self.w(u,v)
        if self.node_degree_list[v]>self.node_degree_list[u]+w:
            self.node_degree_list[v] = self.node_degree_list[u] + w
            self.node_parent_list[v] = u

    def dijkstra(self,s):
        self.initialize(s)
        S = []
        Q = PriorityQueue()
        for d in self.node_degree_list:
            Q.put((self.node_degree_list[d],d))
        while Q.qsize()>0:
            u = Q.get()
            S.append(u[1])
            for v in self.adjacency_list[u[1]]:
                self.relax(u[1],v[0])

    def shortestpath(self,s,d):
        self.dijkstra(s)
        return self.node_degree_list[d]