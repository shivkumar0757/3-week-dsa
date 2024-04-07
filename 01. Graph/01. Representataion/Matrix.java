class Matrix{
    public static void main(String[] args){
        boolean isUndirected = true;
        int numVertices = 5;
        boolean[][] graph = new boolean[numVertices][numVertices];

        int[][] edges = {
            {0, 1}, {0, 4},
            {1, 2}, {1, 3}, {1, 4},
            {2, 3},
            {3, 4}
            // Add more edges as needed
        };

        for (int[] edge : edges){
            int v = edge[0];
            int u = edge[1];

            graph[u][v] = true;
            // for undirected graph
            if (isUndirected)
                graph[v][u] = true;

        }

        // print the materix
        // Print the adjacency matrix
        for (int i = 0; i < numVertices; i++) {
            for (int j = 0; j < numVertices; j++) {
                System.out.print((graph[i][j] ? 1 : 0) + " ");
            }
            System.out.println();
        }
    }
}