def longest_subarray_positives(arr, k):
    n = len(arr)
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(n):
        curr_sum += arr[right]  # expand window

        # shrink from left while sum exceeds k
        while curr_sum > k and left <= right:
            curr_sum -= arr[left]
            left += 1

        # check if current window equals k
        if curr_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len


# Example
arr = [2, 3, 5, 1, 9]
k = 10
print("Longest subarray length:", longest_subarray_positives(arr, k))