# Index search in rotated sorted arrayll
def find_index(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] == target == arr[high]:  # If mid and high are equal, we can't determine the sorted half
            high -= 1  # Reduce the search space
            low += 1  # Increase the search space
        elif arr[mid] <= arr[high]:  # Right half is sorted
            if arr[mid] <= target <= arr[high]:  # Target is in the right half
                low = mid + 1
            else:  # Target is in the left half
                high = mid - 1
        else:  # Left half is sorted
            if arr[low] <= target <= arr[mid]:  # Target is in the left half
                high = mid - 1
            else:  # Target is in the right half
                low = mid + 1
    return -1  # Target not found

arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
result = find_index(arr, target)
if result != -1:
    print("Index of", target, "is", result)
else:
    print("Target not found")