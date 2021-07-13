def quick_sort(array, left, right):
    if left < right:
        position = Partition(array, left, right)
        quick_sort(array, left, position - 1)
        quick_sort(array, position + 1, right)
    return array


def Partition(array, left, right):
    pivot = array[right]  # pick last element as pivot
    low = left - 1
    for i in range(left, right):
        if array[i] <= pivot:
            low += 1
            Swap(array, i, low)

    Swap(array, right, low + 1)
    return low + 1


def Swap(array, i, low):
    temp = array[i]
    array[i] = array[low]
    array[low] = temp


if __name__ == "__main__":
    list1 = [8, 4, 23, 42, 16, 15]
    print(quick_sort(list1, 0, 5))
    list_2 = [20, 18, 12, 8, 5, -2]
    print(quick_sort(list_2, 0, 5))  # [-2, 5, 8, 12, 18, 20]
