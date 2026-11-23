# single element in sorted array
def single_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]

arr = [1, 1, 2, 2, 3, 3, 4]
result = single_element(arr)
print("The single element in the sorted array is:", result)