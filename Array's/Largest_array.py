class LargestArray:
    def largest(self, nums):
        largest_element = nums[0]

        for i in nums:
            if i > largest_element:
                largest_element = i

        return largest_element


obj = LargestArray()

nums = [7, 8, 6, 4, 9, 2, 3, 90]

print(obj.largest(nums))