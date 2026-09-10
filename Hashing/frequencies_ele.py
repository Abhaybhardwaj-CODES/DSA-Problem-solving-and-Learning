class Frequencies:

    def solution(self, nums, dul_nums):

        # Find unique numbers
        for i in nums:

            if i not in dul_nums:
                dul_nums.append(i)

        # Count frequency
        for i in dul_nums:

            count = 0

            for j in nums:

                if i == j:
                    count += 1

            print(f"The frequency of {i} is: {count}")


Obj = Frequencies()

nums = [1, 1, 3, 2, 4, 6, 8, 4, 6, 3, 8]

dul_nums = []

Obj.solution(nums, dul_nums)


