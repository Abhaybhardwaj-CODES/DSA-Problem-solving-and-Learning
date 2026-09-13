class Solution:
    def duplicate_array(self, nums):
        new_array = []

        # Remove duplicates
        for i in range(len(nums)):
            if nums[i] not in new_array:
                new_array.append(nums[i])

        # Sort the new array
        for i in range(len(new_array)):
            min_index = i

            for j in range(i + 1, len(new_array)):
                if new_array[j] < new_array[min_index]:
                    min_index = j

            new_array[i], new_array[min_index] = new_array[min_index], new_array[i]

        return new_array


obj = Solution()

nums = [7, 3, 2, 7, 4, 3, 9, 2]

print(obj.duplicate_array(nums))