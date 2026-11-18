
def countSubarrays(arr, k):
    freq = {0: 1}
    prefix = 0
    count = 0

    for num in arr:
        prefix += num

        required = prefix - k

        count += freq.get(required, 0)

        freq[prefix] = freq.get(prefix, 0) + 1

    return count


arr = [1, 2, 3]
k = 3

print(countSubarrays(arr, k))
