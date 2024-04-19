import java.util.HashMap;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import java.util.HashSet;


public class Bfs{

    public static void main(String args[]){
        int vertices = 5;
        Graph graph = new Graph(vertices);

         // Add edges to the graph
         graph.addEdge(0, 1);
         graph.addEdge(0, 2);
         graph.addEdge(1, 3);
         graph.addEdge(1, 4);
         graph.addEdge(2, 4);
        
         int startPoint = 0;

         System.out.println("BFS for graph, from starting point: " + startPoint);

         graph.bfs(startPoint);

    }

}

class Graph{
    int vertices;
    HashMap<Integer, ArrayList<Integer>> graph = new HashMap<>();

    Graph(int vertices){
        this.vertices = vertices;
        for(int i=0; i < vertices; i++){
            graph.put(i, new ArrayList<>());
        }
    }

    public void addEdge(int u, int v){
        graph.get(u).add(v);
    }

    public void bfs(int startNode){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(startNode);
        HashSet<Integer> visited = new HashSet<>();

        while(!queue.isEmpty()){
            int currElem = queue.poll();
            System.out.println("| "+ currElem);
            visited.add(currElem);

            for(int neighbour: graph.get(currElem)){
                if (!visited.contains(neighbour)){
                    queue.offer(neighbour);
                }
            }
        }
    }
}