# CEILING OF A NUMBER X IN A SORTED ARRAY
def ceiling(arr, x):
    n = len(arr)
    if x > arr[n - 1]:
        return -1  # Ceiling doesn't exist

    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return arr[mid]  # Exact match found
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return arr[low]  # The ceiling value
arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
print("Ceiling of", x, "is", ceiling(arr, x))