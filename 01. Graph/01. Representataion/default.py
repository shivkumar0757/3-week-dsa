# Default Grapth rep contains set of (V, E) where edge is parir of vertices like (v1,v2)
# if all nodes are connected , we can represent by list of edges only

class DefaultGraph:
    def __init__(self):
        self.vertices = set()    #we can also use list/array
        self.edges = set()   #we can also use list/array

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            edge = (vertex1, vertex2)
            self.edges.add(edge)
        else:
            print("One of vertex not found in the graph")


graph = DefaultGraph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2,1)
print(graph.vertices)
print(graph.edges)

