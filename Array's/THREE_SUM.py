def three_sum(arr, target):
    n = len(arr)
    seen = {}

    for i in range(n):
        for j in range(i + 1, n):
            required = target - arr[i] - arr[j]

            if required in seen:
                return [seen[required], i, j]

        seen[arr[i]] = i

    return []
N = [1,2,4,5,78,4,24,8,53,13,78]
target = 87
print(three_sum(N , target))