from data_structures_and_algorithms_python.challenges.hashmap_tree_intersection.hashmap_tree_intersection import *

import pytest


def test_tree_intersection(test_tree):
    expected = '[100, 160, 125, 175, 200, 350, 500]'
    actual = f"{test_tree}"
    assert actual == expected


def test_empty_tree():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    expected = None
    actual = tree_intersection(tree1, tree2)
    assert actual == expected


@pytest.fixture
def test_tree():
    tree1 = Tree_Node(150)
    tree1.left = Tree_Node(100)
    tree1.left.left = Tree_Node(75)
    tree1.left.right = Tree_Node(160)
    tree1.left.right.left = Tree_Node(125)
    tree1.left.right.right = Tree_Node(175)
    tree1.right = Tree_Node(250)
    tree1.right.left = Tree_Node(200)
    tree1.right.right = Tree_Node(350)
    tree1.right.right.left = Tree_Node(300)
    tree1.right.right.right = Tree_Node(500)
    binary_tree1 = BinaryTree(tree1)
    tree2 = Tree_Node(42)
    tree2.left = Tree_Node(100)
    tree2.left.left = Tree_Node(15)
    tree2.left.right = Tree_Node(160)
    tree2.left.right.left = Tree_Node(125)
    tree2.left.right.right = Tree_Node(175)
    tree2.right = Tree_Node(600)
    tree2.right.left = Tree_Node(200)
    tree2.right.right = Tree_Node(350)
    tree2.right.right.left = Tree_Node(4)
    tree2.right.right.right = Tree_Node(500)
    binary_tree2 = BinaryTree(tree2)
    return tree_intersection(binary_tree1, binary_tree2)
