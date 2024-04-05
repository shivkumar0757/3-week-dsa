# we can represnt graph via adjacency list of vertices and lined vertices 

class AdjacencyList:
    
    def __init__(self):
        self.adj_list = dict()

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].add(vertex2)
        else:
            print("vertex1 or vertex2 not present in the graph")


graph = AdjacencyList()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(0,1)
graph.add_edge(1,2)
graph.add_edge(2, 1)
print(graph.adj_list)

