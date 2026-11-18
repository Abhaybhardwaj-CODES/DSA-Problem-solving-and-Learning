
def longestEqual(arr):
    prefix_map = {0: -1}
    prefix = 0
    longest = 0

    for i in range(len(arr)):

        if arr[i] == 0:
            prefix -= 1
        else:
            prefix += 1

        if prefix in prefix_map:
            length = i - prefix_map[prefix]
            longest = max(longest, length)

        else:
            prefix_map[prefix] = i

    return longest


arr = [0, 1, 0, 1, 1, 1, 0]

print(longestEqual(arr))
