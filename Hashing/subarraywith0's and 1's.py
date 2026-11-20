# THE LONGEST SUBARRAY WITH EQUAL NUMBER OF 0'S AND 1'S
def longestEqual(arr):
# PREFIX SUM APPROACH
    prefix_map = {0: -1}
    prefix = 0
    longest = 0
     #In this approach, we will treat 0's as -1 and 1's as +1. The idea is to find the longest subarray with a sum of 0, which indicates an equal number of 0's and 1's.

    for i in range(len(arr)):

        if arr[i] == 0:
            prefix -= 1
        else:
            prefix += 1

            # If the prefix sum has been seen before, it means that the subarray between the previous index and the current index has a sum of 0, indicating an equal number of 0's and 1's. We calculate the length of this subarray and update the longest length if necessary. If the prefix sum has not been seen before, we store the current index in the prefix_map for future reference.

        if prefix in prefix_map:
            length = i - prefix_map[prefix]
            longest = max(longest, length)
            # ELSE, we store the current index in the prefix_map for future reference.

        else:
            prefix_map[prefix] = i

    return longest



arr = [0, 1, 0, 1, 1, 1, 0]

print(longestEqual(arr))
