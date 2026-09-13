class SecondLargest:
    def second_largest(self, nums):
        largest = nums[0]
        second = nums[0]

        for i in nums:
            if i > largest:
                second = largest
                largest = i
            elif i > second and i != largest:
                second = i

        return second


obj = SecondLargest()

nums = [7, 8, 6, 4, 9, 2, 3, 90]

print(obj.second_largest(nums))