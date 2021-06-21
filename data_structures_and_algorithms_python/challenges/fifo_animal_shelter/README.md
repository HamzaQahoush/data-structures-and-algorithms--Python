# Challenge Summary

<!-- Description of the challenge -->

First-in, First out Animal Shelter.

enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.

dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.

## Whiteboard Process

<!-- Embedded whiteboard image -->

![](https://i.ibb.co/ng6dQ7j/code-challenges-8.jpg)

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

I took the approach of creating a class for dog and cat and take instances from Queue class in AnimalShelter class .
I added the attributes name,type for each dog, cat class. and check it in enqueuing and dequeuing

## Solution

<!-- Show how to run your code, and examples of it in action -->

define a class for do and cat which takes name and type for both.

define animal shelter class , and take instance from for cat and dog from the Queue.

define method enqueue which take animal parameter we check for both cases if the type of animal is dog or cat then enqueue it .

define method dequeue which take "pref" as parameter and we check about it if cat or dog then enqueue it .
else return Null.


[Pull Request Link](https://github.com/HamzaQahoush/data-structures-and-algorithms--Python/blob/master/data_structures_and_algorithms_python/challenges/fifo_animal_shelter/fifo_animal_shelter.py)
