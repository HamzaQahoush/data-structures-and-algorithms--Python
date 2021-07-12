# Merge sort 

### The function which will go through it 


• sample array : 

arr= [8 , 4 , 23 , 42 , 16 , 15 ]

```

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

```

### Visualization and trace of code : 

<img src="Merge-Sort trace.png"/>


 **************************

## Efficency
Merge Sort is a recursive algorithm and time complexity can be expressed 

• Time: O(log n)


• Space: O(n)
we have to store the elements somewhere. Additional space complexity can be O(n) in an implementation using arrays .