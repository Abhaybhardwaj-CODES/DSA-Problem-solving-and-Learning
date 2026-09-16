def maxSubArray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(arr))


''' PRINTING THE MAX SUBARRAY'''
def maxSubArray(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):

        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i

    print("Maximum Sum:", max_sum)
    print("Subarray:", arr[start:end + 1])


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSubArray(arr)