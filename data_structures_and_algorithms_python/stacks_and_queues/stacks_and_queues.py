class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

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


class EmptyStackException(Exception):
    pass

class EmptyQueueException(Exception):
    pass


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        new_node= Node(value)
        if not self.front:
            self.front= new_node
            self.rear= new_node
        else:
            self.rear.next=new_node
            self.rear= new_node
                
    def __str__(self):
        current=self.front
        items= []
        while current:
            items.append(str(current.value))
            current=current.next
        return f" <- ".join(items)
        
    def IsEmpty(self): 
        return self.front == None
    def dequeue (self): 
        if not self.front :
            raise EmptyQueueException()
        else:
            temp = self.front
            self.front=self.front.next
            temp.next= None
            return temp.value

    def peek (self): 
        if self.front: 
            return self.front.value
            
        else : 
            raise EmptyQueueException(" Cannot Peek on empty Queue!")
        







# if __name__ == "__main__" :
    # # stack= Stack() 
    # # # print (stack ,)
    # # stack.push(5)
    # # # print(stack ,)
    # # stack.push(4,)
    # # print(stack,)
    # # stack.pop()
    # # print(stack, )
    # # print(stack.peek())
    # queue=Queue()

    # # print (queue , "empty")
    # queue.enqueue('Hamza')
    # # print (queue)
    # queue.enqueue('Moh')
    # queue.enqueue('saed')
    # # queue.dequeue()
    # # print (queue)
    # print(queue.peek())