def create_adj_graph(edges, is_undirected):
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = list()
        if v not in graph:
            graph[v] = list()

        if v not in graph[u]:
            graph[u].append(v)

        if is_undirected and u not in graph[v]:
            graph[v].append(u)
    return graph


edges = [[0,1], [1,2], [2,0]]

graph = create_adj_graph(edges, False)
print(graph)
graph_un = create_adj_graph(edges, True)
print(graph_un)
