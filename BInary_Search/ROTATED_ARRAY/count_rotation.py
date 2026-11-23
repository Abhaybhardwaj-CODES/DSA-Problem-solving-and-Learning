# count the rotation in a sorted and rotated array
def count_rotations(arr):
    low = 0
    high = len(arr) - 1
    n = len(arr)

    while low < high:
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return low
arr = [15, 18, 2, 3, 6, 12]
result = count_rotations(arr)   
print("The array is rotated", result, "times.")