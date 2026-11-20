# Floor of x in a sorted array is the largest element that is smaller than or equal to x.
def floor(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] < x:
            result = arr[mid]
            low = mid + 1

        else:
            high = mid - 1

    return result
  
arr = [2, 6, 34, 90, 665, 2, 5, 6, 9, 3, 63, 25]
arr.sort()
print(floor(arr, 6))       