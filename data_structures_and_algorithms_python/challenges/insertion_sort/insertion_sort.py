def InsertionSort(arr): 
    for i in range (1,len(arr)) : 
        j = i -1       # the marker for sorted element 
        temp = arr[i] # select the first unsorted element

        while j >= 0 and temp < arr[j] : 
            """this loop shifts all the elements to right 
            to create the position for unsorted element
        """
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=temp  # this for insert the unsorted element to its correct position.
    return arr


if __name__ == "__main__":
    arr=[8,4,23,42,16,15]
    print(InsertionSort(arr))
