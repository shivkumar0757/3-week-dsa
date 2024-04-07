def create_matrix_graph(n, edges, is_undirected):
    graph = [[0]*n for _ in range(n)]

    for u, v in edges:
        graph[u][v] = 1

        if is_undirected:
            graph[v][u] = 1

    return graph
    

n = 6
edges = [[0,3], [1,2], [1,5], [2,4], [3,5], [5,4], [5,0]]

graph = create_matrix_graph(n, edges, False)
print(graph)

graph_undirected = create_matrix_graph(n, edges, True)
print(graph_undirected)

