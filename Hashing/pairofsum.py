# pair of sum problem

def countPairs(arr, target):
    freq = {}
    count = 0

    for num in arr:
        required = target - num

        count += freq.get(required, 0)

        freq[num] = freq.get(num, 0) + 1

    return count


arr = [1, 5, 7, -1, 5]
target = 6

print(countPairs(arr, target))
