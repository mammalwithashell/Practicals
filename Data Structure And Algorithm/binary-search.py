def binary_search(arr, value, start=0, end=None):
    if end == None:
        end = len(arr) - 1

    if start <= end:
        middle = int((start + end) / 2)
        if arr[middle] == value:
            return middle
        elif arr[middle] > value:
            return binary_search(arr, value, start, middle - 1)
        else:
            return binary_search(arr, value, middle + 1, end)

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
