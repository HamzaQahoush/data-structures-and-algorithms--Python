# Challenge Summary

<!-- Description of the challenge -->

Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1)

## Whiteboard Process

<!-- Embedded whiteboard image -->

![](https://i.ibb.co/p4CYJBT/code-challenges-4.jpg)

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

define our function which take 2 linked list as paramter
start with head with each list
check if the list if doesn't have value. and raise Exception("lists are empty")
if any of current list don't have head we take the head from other list.
then , we go to next value and set a temp value to current of list2
and looping throw the next values and switch between current next values between lists.
then we check if we don't have current .next for both list 1 and list2
in case if we have not current.next for list 1 , set it to current of list 2 and return list 1 head
in case if we have not current. Next for list 2 , we keep switching and return list 2 head
The Big is still O(1)

## Solution

<!-- Show how to run your code, and examples of it in action -->

Example :
list 1 :

head - > 1 -> 3 -> 2-> x

list 2 :

head - > 5 -> 9 -> 4 -> x

output:

head - > 1 -> 5 -> 3 -> 9 ->2 -> 4 -> x
