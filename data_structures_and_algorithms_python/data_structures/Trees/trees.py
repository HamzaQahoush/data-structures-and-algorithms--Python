#-------------------------Tree implementation 1/2-- Code Challenge: Class 15 ----------------------        
class Tree_Node : 
    def __init__(self , value=None): 
        self.value = value
        self.right= None
        self.left=None

    def __str__(self):
        return str(self.value)


class BinaryTree (Tree_Node) : 
    def __init__(self,root=None): 
        self.root=root

    def pre_order(self):     ## root-> left ->right
        pre_list= []
        if self.root is None : 
            raise Exception("Empty Tree")
        def traverse(root)  : 
            pre_list.append(root.value)
                
            if root.left :
                traverse(root.left )
            if root.right : 
                traverse(root.right)

        traverse(self.root)
        return  (pre_list )


    def in_order(self):   #Left, Root, Right
        in_list=[] 
        if self.root is None : 
            raise Exception("Empty Tree")
        def traverse(root): 
            if root.left: 
                traverse(root.left)
            in_list.append (root.value)

            if root.right: 
                traverse(root.right)    

        traverse (self.root)
        return (in_list ) 


    def post_order(self, root):
        res = []
        if root:
            res = res + self.post_order(root.left)
            res = res + self.post_order(root.right)
            res.append(root.value)
        
        return res 

#------------------------- find max in tree -- Code Challenge: Class 16 ----------------------        
    def tree_max(self): 
        max =0
        if not self.root.value : 
            return "No Max Value empty Tree"
            
        else:
            
            mylist = self.in_order()
            for i in mylist : 
                if i > max:  
                    max= i
        return max
#-------------------------Breadth-first Traversal-- Code Challenge: Class 17 ----------------------        


    def breadth_first(tree): 

        if tree.root is None :
            return "empty"

        else :     
            result=[]
            queue = []    
            queue+=[tree.root]            
            while queue : 
                currentNode = queue[0]
                if currentNode.left: 
                    queue+=[currentNode.left]
                if currentNode.right: 
                    queue+=[currentNode.right]

                result += [queue.pop(0).value]

            
        return result    

            

#-------------------------Tree implementation 2/2-- Code Challenge: Class 15 ----------------------        


class  Binary_Search (BinaryTree) : 

    def add(self,value) : 
        if self.root: 
            def traverse(root):
                if value < root.value: 
                    if root.left is None :
                        root.left=Tree_Node(value)
                        return
                        
                    else: 
                        traverse(root.left)   

                elif value > root.value: 
                    if root.right is None :
                        root.right=Tree_Node(value)
                        return
                    else : 
                        traverse(root.right) 

            return traverse(self.root)
        else:
            self.root=Tree_Node(value)
        




    def contains(self,value):
        if not self.root:
            return False
        def traverse(root):
            if root:
                if root.value == value:
                    return True 
                if traverse(root.left):
                    return True
                if traverse(root.right):
                    return True
            return False
        return traverse(self.root)


#--------------------------------------------------------------------------------------


if __name__ == "__main__":
    node1 = Tree_Node(1)
    node1.left = Tree_Node(2)
    node1.right = Tree_Node(3)
    node1.left.left = Tree_Node(4)
    node1.left.right = Tree_Node(5)
    binary_tree = BinaryTree(node1)
    # print(binary_tree.tree_max())

    print(binary_tree.breadth_first())
    # print(binary_tree.pre_order())  #1, 2, 4, 5, 3 
    # print (binary_tree.in_order()) #4, 2, 5, 1, 3
    # print (binary_tree.post_order(node1)) #4, 5, 2, 3, 1
    

    # valueInsert = Binary_Search()
    # valueInsert.add(3)
    # valueInsert.add(6)
    # valueInsert.add(14)
    # valueInsert.add(15)
    # valueInsert.add(16)
    # valueInsert.add(17)
    # valueInsert


   
