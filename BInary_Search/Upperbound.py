# UPPERBOUND binnary search
def upper_bound(arr, x):
    low = 0
    high = len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1

    return low
arr = [2, 6, 34, 90, 665, 2, 5, 6, 9, 3, 63, 25]
arr.sort()
target = 6
print(upper_bound(arr, target))