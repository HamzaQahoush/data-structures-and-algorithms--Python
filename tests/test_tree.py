from data_structures_and_algorithms_python.Trees.trees import * 
import pytest 


# 1. Can successfully instantiate an empty tree
def test_instance_an_empty_tree():
    tree = BinaryTree()
    assert isinstance(tree, BinaryTree)     


#2. Can successfully instantiate a tree with a single root node
def test_single_root_node (): 
    expected =5
    value=Binary_Search(5)
    actual=value.root
    assert actual == expected

# 3.Can successfully add a left child and right child to a single root node

def test_add_left_and_right_child_to_single_root_node(): 
    expected =  [2, 1, 3]
    node1 = Tree_Node(1)
    node1.left = Tree_Node(2)
    node1.right = Tree_Node(3)
    binary_tree = BinaryTree(node1)
    actual= binary_tree.in_order()
    assert actual == expected
    

# 4.Can successfully return a collection from a preorder traversal
def test_return_a_collection_from_a_preorder_traversal(tree_test): 
    expected = '3, 12, 4, 5, 2, 1, 6'
    actual =tree_test.pre_order()
    assert actual == expected

# 4.Can successfully return a collection from a in_order traversal
def test_return_a_collection_from_a_In_order_traversal(tree_test): 
    expected = [4, 12, 5, 3, 1, 2, 6]
    actual =tree_test.in_order()
    assert actual == expected   

# 4.Can successfully return a collection from a post_order traversal
def test_return_a_collection_from_a_post_order_traversal():

    node1 = Tree_Node(1)
    node1.left = Tree_Node(2)
    node1.right = Tree_Node(3)
    node1.left.left = Tree_Node(4)
    node1.left.right = Tree_Node(5)
    binary_tree = BinaryTree(node1)
    expected =  [4, 5, 2, 3, 1]
   
    actual =binary_tree.post_order(node1)
    assert actual == expected    
    



#5. find a max in tree 
def test_max_in_tree (tree_test) : 
    expected = 12
    actual =tree_test.tree_max()
    assert actual == expected   

def test_max_empty_in_tree () : 
    node1= Tree_Node()
    binary_tree = BinaryTree(node1)
    expected = "No Max Value empty Tree"
    actual =binary_tree.tree_max()
    assert actual == expected   



@pytest.fixture
def tree_test():
    node1 = Tree_Node(3)
    node1.left = Tree_Node(12)
    node1.left.right = Tree_Node(5)
    node1.left.left = Tree_Node(4)
    node1.right = Tree_Node(2)
    node1.right.left = Tree_Node(1)
    node1.right.right = Tree_Node(6)
    binary_tree = BinaryTree(node1)
    return binary_tree    