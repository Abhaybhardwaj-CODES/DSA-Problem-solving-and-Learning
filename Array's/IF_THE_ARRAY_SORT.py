class solution:
    def check_sort(self , nums):
          for i in range(len(nums) - 1):
               if nums[i] > nums[i + 1]:
                 return False

          return True     

obj = solution()

nums = [2, 3, 4, 6, 7, 8, 9, 90]

print(obj.check_sort(nums))    