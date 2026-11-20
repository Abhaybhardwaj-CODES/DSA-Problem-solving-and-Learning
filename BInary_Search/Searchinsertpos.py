# search insert position
def search_insert_position(arr, target):
    n = len(arr)

    st = 0
    end = n - 1

    while st <= end:

        mid = (st + end) // 2

        if target > arr[mid]:
            st = mid + 1

        elif target < arr[mid]:
            end = mid - 1

        else:
            return mid

    return st
arr = [2, 6, 34, 90, 665, 2, 5, 6, 9, 3, 63, 25]
arr.sort()
target = 1
print(search_insert_position(arr, target))