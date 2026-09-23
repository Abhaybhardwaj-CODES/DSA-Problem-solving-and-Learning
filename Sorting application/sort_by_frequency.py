from collections import Counter

def sort_by_frequency(arr):
    freq = Counter(arr)

    arr.sort(key=lambda x: (-freq[x], x))

    return arr


arr = [4, 6, 2, 6, 4, 4, 6, 2]

print(sort_by_frequency(arr))