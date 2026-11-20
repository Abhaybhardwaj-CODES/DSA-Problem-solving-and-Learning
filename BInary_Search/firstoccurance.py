# First occurrence of an element in a sorted array using binary search
def first_occurrence(arr, target):
    n = len(arr)

    st = 0
    end = n - 1
    result = -1

    while st <= end:

        mid = (st + end) // 2

        if target > arr[mid]:
            st = mid + 1

        elif target < arr[mid]:
            end = mid - 1

        else:
            result = mid
            end = mid - 1

    return result       
arr = [2, 6, 34, 90, 665, 2, 5, 6, 9, 3, 63, 25]
arr.sort()
print(first_occurrence(arr, 6))