import java.util.ArrayList;
import java.util.HashSet;

class DefaultGraph{
    private HashSet<Integer> vertices = new HashSet<>();
    private HashSet<ArrayList<Integer>> edges = new HashSet<>();

    public void addVertex(Integer vertex){
        vertices.add(vertex);
    }

    public void addEdge(Integer vertex1, Integer vertex2){
        if (vertices.contains(vertex1) && vertices.contains(vertex2)){
            ArrayList<Integer> edge = new ArrayList<>();
            edge.add(vertex1);
            edge.add(vertex2);
            edges.add(edge);
        }
        else{
            System.out.println("One of edge not present in the graph");
        }
    }

    public HashSet<Integer> getVertices(){
        return vertices;
    }

    public HashSet<ArrayList<Integer>> getEdges(){
        return edges;
    }
}

public class Default{
    public static void main(String args[]){
        DefaultGraph graph = new DefaultGraph();
        graph.addVertex(0);
        graph.addVertex(1);
        graph.addVertex(2);
        graph.addEdge(0,1);
        graph.addEdge(1,2);
        graph.addEdge(2, 1);
        System.out.println(graph.getVertices());
        System.out.println(graph.getEdges());

    }
}