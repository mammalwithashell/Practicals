'''

Most Important is the best case scenario when it takes only O(N).
All other cases O(N^2)

When a sorted list is passed the inner for loop will compare with all N elements but swap takes place leaving the swapped flag false.

After each iteration the last element in array is the largest element.

In sorted list, bubble sort is alway faster than quicksort,mergesort or any other sorting counterpart( O(N*LogN) ).

Resources :

    https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif

'''


def bubble_sort(arr):
    swapped = True  # For initial entry in array
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True


arr = [6, 5, 4, 3, 2, 1]
bubble_sort(arr)
print(arr)
