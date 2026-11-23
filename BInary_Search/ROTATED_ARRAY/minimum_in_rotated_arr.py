# MINIMUM ELEMENT IN ROTATED SORTED ARRAY
def minimum_in_rotated_array(arr):
    low = 0
    n = len(arr)
    high = n - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            high = mid 
        else:
            low = mid + 1
    return arr[low]

arr = [3, 4, 5, 1, 2]
result = minimum_in_rotated_array(arr)
print("Minimum element in the rotated sorted array is:", result)
 