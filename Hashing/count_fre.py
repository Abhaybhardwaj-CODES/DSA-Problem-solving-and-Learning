class Solution:

    def countFrequencies(self, nums, n):

        count = 0

        for i in nums:
            if i == n:
                count = count + 1

        print(f"The frequency of {n} is: {count}")


obj = Solution()

nums = [1, 2, 2, 1, 3]

n = int(input("Enter the number you want to find the frequency of: "))

obj.countFrequencies(nums, n)

