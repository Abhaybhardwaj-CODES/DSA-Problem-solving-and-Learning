def next_permutation(arr):
    n = len(arr)

    # 1. Find the first decreasing element from right
    i = n - 2

    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    # 2. If such element exists, find next greater element
    if i >= 0:
        j = n - 1

        while arr[j] <= arr[i]:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

    # 3. Reverse the remaining part
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr


arr = [1, 2, 3]
print(next_permutation(arr))