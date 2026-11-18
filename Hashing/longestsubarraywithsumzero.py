
def longestSubarray(arr):
    prefix_map = {0: -1}
    prefix = 0
    longest = 0

    for i in range(len(arr)):
        prefix += arr[i]

        if prefix in prefix_map:
            length = i - prefix_map[prefix]
            longest = max(longest, length)

        else:
            prefix_map[prefix] = i

    return longest


arr = [1, 2, -2, 4, -4]

print(longestSubarray(arr))
