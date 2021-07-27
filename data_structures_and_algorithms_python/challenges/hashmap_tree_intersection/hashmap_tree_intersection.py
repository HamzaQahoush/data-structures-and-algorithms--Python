from data_structures_and_algorithms_python.data_structures.Trees.trees import *


def tree_intersection(tree1, tree2):
    result = list()
    if tree1.root is None and tree2.root is None:
        return None

    def traverse(root1, root2):
        if root1.value == root2.value:
            nonlocal result
            result += [root1.value]
        if root1.left and root2.left:
            traverse(root1.left, root2.left)
        if root1.right and root2.right:
            traverse(root1.right, root2.right)
    traverse(tree1.root, tree2.root)
    return result


if __name__ == "__main__":
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
    print(binary_tree1.pre_order())
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
    print(binary_tree2.pre_order())
    print(tree_intersection(binary_tree1, binary_tree2))
