class Solution:
    def left_rotate(self, arr, k):
        n = len(arr)

        # If k is greater than array length
        k = k % n

        # Store first k elements
        temp = arr[:k]

        # Shift remaining elements to the left
        for i in range(k, n):
            arr[i - k] = arr[i]

        # Put first k elements at the end
        for i in range(k):
            arr[n - k + i] = temp[i]

        return arr


obj = Solution()

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2

print(obj.left_rotate(arr, k))