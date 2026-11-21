# index search in rotated sorted array ll 
def search_rotated_II(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        # Remove ambiguity caused by duplicates
        if (arr[low] == arr[mid] ==
                arr[high]):
            low += 1
            high -= 1
            continue

        # Left half is sorted
        if arr[low] <= arr[mid]:

            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half is sorted
        else:

            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False
arr = [3 , 3, 3, 1 ,3 , 3, 3]
target = 1
result = search_rotated_II(arr, target)
if result:
    print("Target", target, "found in the array.")
else:
    print("Target", target, "not found in the array.")