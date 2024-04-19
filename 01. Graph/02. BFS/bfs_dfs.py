from collections import defaultdict, deque

# Procedure BFS(u):
#     Initialize an empty queue and add the starting node (u) to it
#     Initialize an empty set to keep track of visited nodes and add the starting node (u) to it

#     While the queue is not empty:
#         Print the current state of the queue
#         Remove the first element from the queue and assign it to a variable (curr_elem)
#         Print the current element (curr_elem)

#         For each neighbour of the current element (curr_elem) in the adjacency list:
#             If the neighbour has not been visited:
#                 Add the neighbour to the visited set
#                 Add the neighbour to the end of the queue

## Procedure DFS(u, visited, graph):
                    #     Print the current node (u)
                    #     Add the current node (u) to the visited set

                    #     For each neighbour of the current node (u) in the adjacency list:
                    #         If the neighbour has not been visited:
                    #             Recursively call DFS on the neighbour
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def bfs(self, u):
        queue = deque()
        # we can also use the Array as we know the number of nodes
        visited = set()

        queue.append(u)
        visited.add(u)

        while queue:
            print(queue)
            curr_elem = queue.popleft()
            print(curr_elem, end = ' || ')

            for neighbour in self.adj_list[curr_elem]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def dfs(self, u, visited, graph):
        print(u)
        visited.add(u)

        for neighbour in graph[u]:
            if neighbour not in visited:
                self.dfs(neighbour, visited, graph)

    def dfs_stack(self, start):
        stack = [start]
        visited = set()

        while stack:
            vertex = stack.pop()
            print(vertex, end = ' || ')

            if vertex not in visited:
                visited.add(vertex)

                for neighbour in self.adj_list[vertex]:
                    if neighbour not in visited:
                        stack.append(neighbour)


graph = Graph()

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)

start_point = 0
print(graph.adj_list)
graph.bfs(start_point)
print('\n---BFS below----')
graph.dfs(start_point, set(), graph.adj_list)

       