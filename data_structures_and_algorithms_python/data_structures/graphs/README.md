# Graphs
<!-- Short summary or background information -->
A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

Here is some common terminology used when working with Graphs:

• Vertex - A vertex, also called a “node”, is a data object that can have zero or more adjacent vertices.

• Edge - An edge is a connection between two nodes.

• Neighbor - The neighbors of a node are its adjacent nodes, i.e., are connected via an edge.

•  Degree - The degree of a vertex is the number of edges connected to that vertex.


## Challenge
<!-- Description of the challenge -->
Implementation  of graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this 
approach? -->
Big O :
Time : O(1)
Space : O(1)
## API :
* add node
    - Arguments: value
    - Returns: The added node
    - Add a node to the graph
 * add edge
    - Arguments: 2 nodes to be connected by the edge, weight (optional)
    - Returns: nothing
    - Adds a new edge between two nodes in the graph
    - If specified, assign a weight to the edge
    - Both nodes should already be in the Graph
 * get nodes
    - Arguments: none
    - Returns all of the nodes in the graph as a collection (set, list, or similar)
 * get neighbors
    - Arguments: node
    - Returns a collection of edges connected to the given node
    - Include the weight of the connection in the returned collection
 * size
    - Arguments: none
    - Returns the total number of nodes in the graph


## Tasks checklist:
- [x] Top-level README “Table of Contents” is updated
- [x] Feature tasks for this challenge are completed
- [x] Unit tests written and passing
- [x] “Happy Path” - Expected outcome
- [x] Expected failure
- [x] Edge Case (if applicable/obvious)
- [x] README for this challenge is complete
- [x] Description, Approach & Efficiency, Solution
- [x] Link to code

[code](graph.py)


