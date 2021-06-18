import pytest
import re
from _pytest.python_api import raises
from data_structures_and_algorithms_python.stacks_and_queues.stacks_and_queues import *


def test_instance_stack() : 
    stack = Stack()
    assert isinstance (stack,Stack)


# test 1: Can successfully push onto a stack

def test_push_stack():
    stack= Stack()
    stack.push('Hi')
    actual = f"{stack}"
    expected = 'Hi'
    assert actual == expected

# test 2 Can successfully push multiple values onto a stack
def test_push_multiple_values_stack(stack_values):
    
    expected = '6 -> 4 -> 7 -> 8'
    actual = f"{stack_values}"
    assert actual == expected

# test 3 Can successfully pop off the stack
def test_pop_stack(stack_values): 
    poped =stack_values.pop()
    assert poped == 6


# test 4 Can successfully empty a stack after multiple pops
def test_empty_stack_after_multiple_pops(stack_values) : 
    for i in range(4): 
        stack_values.pop()
    assert "The stack is empty "

# test 5 Can successfully peek the next item on the stack
def test_peek_the_next_item_stack(stack_values): 
    expected = 4 
    actual=stack_values.top.next.value
    assert actual == expected


# test 6 Can successfully instantiate an empty stack

def test_instance_stack() : 
    stack = Stack()
    assert isinstance (stack,Stack)


# test 7 Calling pop or peek on empty stack raises exception
def test_pop_or_peek_on_empty_stack_raises_exception(): 
    stack= Stack() 
    with pytest.raises(EmptyStackException) :
        stack.peek()



# test 8: Can successfully enqueue into a queue
def test_queue_enqueue(): 
    queue= Queue()
    queue.enqueue('6')
    actual = f"{queue}"
    expected = '6'
    assert actual == expected


# test 9: Can successfully enqueue multiple values into a queue

def test_q_multiple_enqueue(queue_values): 
    expected ='8 <- 7 <- 4 <- 6'
    actual = f'{queue_values}'
    assert actual == expected

# test 10: Can successfully dequeue out of a queue the expected value

def test_dequeue (queue_values)  : 
    data= queue_values.dequeue()
    assert data== 8
    assert queue_values.front.value == 7

# test 11 : Can successfully peek into a queue, seeing the expected value

def test_peek_q (queue_values) : 
    value= queue_values.peek()
    assert value== 8
    



# test 12: Can successfully empty a queue after multiple dequeues


def test_empty_queue (queue_values) : 
    for count in range (4) : 
        queue_values.dequeue()

    with pytest.raises(EmptyQueueException) : 
        queue_values.dequeue()
        



# test 13 Can successfully instantiate an empty queue
def test_instance():
    queue = Queue()
    assert isinstance(queue, Queue) 


# test 14 Calling dequeue or peek on empty queue raises exception

def test_peek_empty_Q () : 
    queue= Queue()
    with pytest.raises(EmptyQueueException):
        queue.peek()



@pytest.fixture
def stack_values() : 
    stack=Stack()
    stack.push(8)        
    stack.push(7)        
    stack.push(4)        
    stack.push(6)   
    print (stack)   
    return stack


@pytest.fixture
def queue_values() : 
    queue= Queue()
    queue.enqueue(8)
    queue.enqueue(7)
    queue.enqueue(4)
    queue.enqueue(6)
    return queue

