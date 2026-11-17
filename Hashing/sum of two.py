
def twoSum(nums, target):
    hashmap = {}
    

    for i in range(len(nums)):
        # LOGIC BEHIND THE TWO SUM PROBLEM
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
