# Singly Linked List

A linked list is a sequence of data structures, which are connected together via links.

Linked List is a sequence of links which contains items. Each link contains a connection to another link. Linked list is the second most-used data structure after array. Following are the important terms to understand the concept of Linked List.

Link − Each link of a linked list can store a data called an element.

Next − Each link of a linked list contains a link to the next link called Next.

LinkedList − A Linked List contains the connection link to the first link called First.

## Challenge

It was diffcult to grap the idea of linked list and perform its concept in code.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I use the approach of creating Classes and methods to perfrom this challenge .
also we need if statements and while loops .

When accessing elements of a linked list, speed is proportional to size of the list with Big O(n)

• When inserting a node into the beginning of the list, it only involves creating a new node with an address that points to the old head.

The time it takes to perform this is not dependent on the size of the list. This means that it will be constant time or a Big O(1).

• When inserting a node into the beginning of the list, it only involves creating a new node with an address that points to the old head. The time it takes to perform this is not dependent on the size of the list. This means that it will be constant time or a Big O(1).

## API

<!-- Description of each method publicly available to your Linked List -->

append method : to add node at last of linked list.

insert method :to add node at head of linked list.

include : to check of value of nodes in linked listand return True , False

**str** : return a string with specfic from with values.

insert method before or after specfic value.

### Linked list

- [x] insert at begining
- [x] append at last of linked list
- [x] insert before specfic value
- [x] insert after specfic value
- [x] test if a value included.

### White Boarding

### ll-kth-from-end

![](https://i.ibb.co/Tk7s0Bh/code-challenges-3.jpg)

### append :

![](https://i.ibb.co/Yck7FGx/code-challenges.jpg)

### insert after :

![](https://i.ibb.co/xGD3Pq2/code-challenges-1.jpg)

insert before :

![](https://i.ibb.co/mv1yWDK/code-challenges-2.jpg)
