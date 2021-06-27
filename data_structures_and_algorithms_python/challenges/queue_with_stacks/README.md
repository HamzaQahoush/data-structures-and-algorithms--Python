# Challenge Summary:

### Implement a Queue using two Stacks.

## Whiteboard Process

![](https://i.ibb.co/k8G40Ld/code-challenges-7.jpg)

<!-- Embedded whiteboard image -->

## Approach & Efficiency

The approach which I took in `enqueue` is to push a value in it
for the `dequeue` I poped all elements and push then again and then poped the top.

## Solution

<!-- Show how to run your code, and examples of it in action -->

firstly we need to define our new class Pseudo Queue which takes two stacks and we take an instantons from our original stack .

then we define a method which takes a value and put it at the end of our queue . and for that we can use push method to add the at the end of queue .

after that we need to define another method dequeue which remove the first element from stacks .

make a validation if stacks are empty .
then I looped over the stack 1 top and popped all values and push them in the 2nd stack .
then the popped / dequeued value will be on the top of pushed stack.

after that we need to retrieve the new stack after popping/dequeuing ,
create temporary value which take the stack2
create new instance from it .
popped it again pushed it to to stack 1




[code link](https://github.com/HamzaQahoush/data-structures-and-algorithms--Python/blob/master/data_structures_and_algorithms_python/challenges/queue_with_stacks/queue_with_stacks.py)
