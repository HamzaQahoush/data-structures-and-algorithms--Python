# Challenge Summary
<!-- Description of the challenge -->
 Implement a breadth-first traversal on a graph.




## Approach & Efficiency


## Solution
<!-- Show how to run your code, and examples of it in action -->
<img src= "https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-35/resources/assets/BreadthFirst.PNG">



The visual above shows the levels in which the nodes will be added to the queue. we can see that since the root node is A, it will look the nodes that are only 1 away from the root. This is C,E, & B.

Next it will look at the nodes that are 2 away from the root, this is F, G, & D. It will follow this pattern until it reaches the end of the graph and all nodes have been visited.

[code](graph_breadth_first.py)

