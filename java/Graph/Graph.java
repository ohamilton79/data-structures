package src;

import java.util.*;

public class Graph {

    public static void main(String[] args) {
        //Create a new graph
        Dictionary<String, Node> graph = new Hashtable<String, Node>();
        graph.put("A", new Node("A", new String[]{"B", "F"}));
        graph.put("B", new Node("B", new String[] {"A", "G"}));
        graph.put("C", new Node("C", new String[] {"D", "E", "G"}));
        graph.put("D", new Node("D", new String[] {"C"}));
        graph.put("E", new Node("E", new String[] {"C", "F"}));
        graph.put("F", new Node("F", new String[] {"A", "E"}));
        graph.put("G", new Node("G", new String[] {"B", "C"}));

        //Traverse the graph
        traverseBf(graph, "A");
        traverseDf(graph, "A");
    }

    //Perform breadth-first search
    public static void traverseBf(Dictionary<String, Node> graph, String firstVertexName) {
        //Create a queue to push vertices onto
        Queue<Node> vertexQueue = new LinkedList<Node>();

        //Create a list of visited vertices
        List<Node> visited = new LinkedList<Node>();

        //Set the first vertex as A
        Node currentVertex = graph.get(firstVertexName);

        //1. Push the current vertex (the first vertex is (A)) onto the queue
        vertexQueue.add(currentVertex);

        while (vertexQueue.size() != 0) {

            //Output vertex value and mark as visited if not already
            if (!visited.contains(currentVertex)) {
                System.out.println(currentVertex.value);
                visited.add(currentVertex);
            }

            //2. Keep visiting unvisited vertices connected to the first Node
            for (String vertex : currentVertex.connectedVertices) {
                Node newVertex = graph.get(vertex);

                if (!(visited.contains(newVertex))) {
                    //Push onto vertex queue
                    vertexQueue.add(newVertex);
                }
            }

            //3. Once all the vertices connected to this vertex have been visited, pop the vertex at the start of the queue
            currentVertex = vertexQueue.poll();
            //System.out.println("AAA" + vertexQueue.size());
        }
    }

    //Perform depth-first search
    public static void traverseDf(Dictionary<String, Node> graph, String firstVertexName) {
        //Create a stack to push visited vertices onto
        Stack<Node> vertexStack = new Stack<Node>();

        //Create a list of visited vertices
        List<Node> visited = new LinkedList<Node>();

        //Set the first vertex as A
        Node currentVertex = graph.get(firstVertexName);

        //1. Push the current vertex (A) onto the stack
        vertexStack.push(currentVertex);

        while (vertexStack.size() > 0) {
            //If not already visited, mark as visited and output
            if (!(visited.contains(currentVertex))) {
                System.out.println(currentVertex.value);
                visited.add(currentVertex);
            }

            //2. Keep visiting unvisited vertices connected to the vertex on the top of the stack
            for (String vertex: currentVertex.connectedVertices) {
                Node newVertex = graph.get(vertex);

                if (!(visited.contains(newVertex))) {
                    //3. Push the adjacent vertex onto the stack
                    vertexStack.push(newVertex);
                }
            }

            try {
                currentVertex = vertexStack.pop();
            } catch (EmptyStackException e) {

            }
        }
    }
}
