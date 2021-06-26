# Trees

<!-- Short summary or background information -->

A tree data structure is defined as a collection of objects or entities known as nodes that are linked together to represent or simulate hierarchy.
A tree data structure is a non-linear data structure because it does not store in a sequential manner. It is a hierarchical structure as elements in a Tree are arranged in multiple levels.

![](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/images/BinaryTree1.PNG)
In the Tree data structure, the topmost node is known as a root node. Each node contains some data, and data can be of any type. In the above tree structure, the node contains the name of the employee, so the type of data would be a string.
Each node contains some data and the link or reference of other nodes that can be called children.

## Challenge

<!-- Description of the challenge -->

• Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

• Create a Binary Tree class
Define a method for each of the depth first traversals:

1.pre order

2.in order.

3.post order which returns an
array of the values, ordered appropriately.

• Create a Binary Search Tree class have contain and add method.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

firstly we create a node for tree which contain a value, right, left pointers.

then we create a class for tree to add the methods .
we use recursion approach to traverse over the the node.

## API

<!-- Description of each method publicly available in each of your trees -->

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)

Depth First Traversals:

(a) Inorder (Left, Root, Right) : 4 2 5 1 3

(b) Preorder (Root, Left, Right) : 1 2 4 5 3

(c) Postorder (Left, Right, Root) : 4 5 2 3 1

• contains : which check if a value exist in our tree.

• add method : to add node in a tree using binary search Tree.
