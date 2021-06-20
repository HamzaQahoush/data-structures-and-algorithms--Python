class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
    def __str__(self):
        return self.value    
class EmptyStackException(Exception):
    pass

class EmptyQueueException(Exception):
    pass

class Stack:
    def __init__(self,node=None):
        self.top=node

    def push(self,value):
        if not self.top:
            self.top=Node(value)
        else : 
            new_node= Node(value)
            new_node.next= self.top
            self.top=new_node

    def pop (self):
        if not self.top :
            return "The stack is empty "
        else : 
            temp=self.top
            self.top=self.top.next
            temp.next=None
        return temp.value

    def IsEmpty (self):
        return self.top==None

    def peek(self):
        if self.top:
            return self.top.value
        else :
            raise EmptyStackException(" Cannot Peek on empty stack")
            
    def __str__(self):
        current=self.top
        items= []
        while current:
            items.append(str(current.value))
            current=current.next
        return f" -> ".join(items)

# ----------------------------------------------------------------
class PseudoQueue():
    def __init__ (self,) : 
        self.stack1= Stack()
        self.stack2= Stack()



    def enqueue(self,value): 
        self.stack1.push(value)


    def dequeue(self):  
        if not self.stack1.top and not self.stack2.top : 
            return "can't dequeue from empty stack "
            
        while self.stack1.top : 
            first_top= self.stack1.pop()
            self.stack2.push(first_top)

        result= self.stack2.pop()
        temp= self.stack2 
        self.stack2=Stack()
        while temp.top: 
            temp_top=temp.pop()
            self.stack1.push(temp_top)
        return result    
                

    def __str__(self):
        current=self.stack1.top
        items= []
        while current:
            items.append(str(current.value))
            current=current.next
        return f" -> ".join(items)        








if __name__== "__main__" :
    pesudoQ= PseudoQueue()
    pesudoQ.enqueue(1)
    pesudoQ.enqueue(2)
    pesudoQ.enqueue(3)
    pesudoQ.enqueue(4)
    print(pesudoQ)
    print(pesudoQ.dequeue())
    print(pesudoQ)