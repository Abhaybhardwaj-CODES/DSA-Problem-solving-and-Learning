# COUNT the occurance of an element in a sorted array using binary search
def count_occurrence(arr, target):
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

    if result == -1:
        return 0

    first_occurrence_index = result

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
            st = mid + 1

    last_occurrence_index = result

    return last_occurrence_index - first_occurrence_index + 1
arr = [2, 6, 34, 90, 665, 2, 5, 6, 9, 3, 63, 25]
arr.sort()
print(count_occurrence(arr, 6))