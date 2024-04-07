import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class AdjList {

    private static HashMap<Integer, List<Integer>> createAdjList(Integer[][] edges, Boolean isUndirected){

        HashMap<Integer, List<Integer>> graph = new HashMap<>();

        for(Integer[] edge: edges){
            Integer u = edge[0];
            Integer v = edge[1];

            if (!graph.containsKey(u)){
                graph.put(u, new ArrayList<>());
            }
            if (!graph.containsKey(v)){
                graph.put(v, new ArrayList<>());
            }
            graph.get(u).add(v);
            if (isUndirected){
                graph.get(v).add(u);
            }
        }
        return graph;

    }

    public static void main(String[] args){
        Integer[][] edges = {{0,1}, {1,2}, {2,0}};

        HashMap<Integer, List<Integer>> graph = createAdjList(edges, false);
        System.out.println(graph);

        HashMap<Integer, List<Integer>> graphUndirected = createAdjList(edges, true);
        System.out.println(graphUndirected);



    }
    
}
