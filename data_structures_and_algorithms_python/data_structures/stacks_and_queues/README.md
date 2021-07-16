# Stacks and Queues

<!-- Short summary or background information -->

Stacks and Queues
Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.

Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

![](https://imgs.developpaper.com/imgs/3169162767-5c88cc850daa1_articlex.jpg)

## Challenge

Implementation of Stacks and Queues

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The approach which I used was creating class for Queue and stack and creat the constructor function and defining the method of it . and create instances from it .

## API

<!-- Description of each method publicly available to your Stack and Queue-->

### Creating methods for **stacks** :

**_Push_** : which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.

**_pop_** method removes the node from the top of the stack, and returns the node’s value.

**_peek_** returns the value of the node located on top of the stack.

<!-- Description of the challenge -->

**_isEmpty_** returns a boolean indicating whether or not the stack is empty.

### Creating methods for **Queue** :

**_enqueue_** which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.

**_dequeue_** that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
Should raise exception when called on empty queue.

**_peek_** does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.

**_IsEmpty_** takes no argument, and returns a boolean indicating whether or not the queue is empty.
