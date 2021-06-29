class Node : 
    def __init__(self,value): 
        self.value = value
        self.child = []

    def __str__(self):
        return str(self.value)


class KAryTree : 
    def __init__(self): 
        self.root= None

"""This code done with help from Ahmad Zatar"""

def fizz_Buzz_Tree(KAryTree): 

    def traverse(node):
        if node.child : 
            for i in range(len(node.child)): 
                traverse (node.child[i])

                if node.child[i].value %5 == 0 and\
                node.child[i].value % 3 == 0:
                    node.child[i].value= "Fizz Buzz"
                elif node.child[i].value %5 == 0 : node.child[i].value= "Buzz"
                elif node.child[i].value %3 == 0 : node.child[i].value= "Fizz"
                else: node.child[i].value =str(node.child[i].value)
    traverse(KAryTree.root)            
    if KAryTree.root.value %5 == 0 and\
    KAryTree.root.value %3 ==0 : 
        KAryTree.root.value ="Fizz Buzz"
    if KAryTree.root.value %5 == 0 : KAryTree.root.value ="Buzz"
    if KAryTree.root.value %3 ==0 : KAryTree.root.value ="Fizz"
    else : KAryTree.root.value= str(KAryTree.root.value)

    return KAryTree


if __name__ == "__main__":

    kAryTree = KAryTree()
    kAryTree.root=Node(1) #root
    kAryTree.root.child+=[Node(2)] #child 0
    kAryTree.root.child+=[Node(3)] #child 1
    kAryTree.root.child+=[Node(5)] #child 2
    kAryTree.root.child[0].child+=[Node(5)] #child[0,0]

    fizz_Buzz_Tree(kAryTree)
    print(kAryTree.root.child[0].value) # 2 -> 2 
    print(kAryTree.root.child[1].value) #  3 -> Fizz
    print(kAryTree.root.child[0].child[0].value) # 5 -> Buzz