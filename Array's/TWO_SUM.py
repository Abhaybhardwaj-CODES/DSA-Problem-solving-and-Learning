def two_sum_brute(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

arr = [2, 7, 11, 15]
target = 9
print(two_sum_brute(arr, target))  # [0, 1]