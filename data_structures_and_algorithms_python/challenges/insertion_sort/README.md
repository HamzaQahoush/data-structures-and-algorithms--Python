# Challenge Summary
<!-- Description of the challenge -->
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. 

The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.


## Whiteboard Process
<!-- Embedded whiteboard image -->

<img src="code challenges 26.jpg"/>

## Approach & Efficiency
This is an in-place comparison-based sorting algorithm.
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
• Time: O(n^2)

The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.


• Space: O(1)
No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).

## Solution
<!-- Show how to run your code, and examples of it in action -->
![](https://he-s3.s3.amazonaws.com/media/uploads/46bfac9.png)