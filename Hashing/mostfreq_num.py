class Frequencies:

    def solution(self, nums, dul_nums):
        

        # Find unique numbers
        for i in nums:
            

            if i not in dul_nums:
                dul_nums.append(i)
        Most_frequent = None
        max_count = 0
        # Count frequency
        for i in dul_nums:

            count = 0

            for j in nums:

                if i == j:
                    count += 1

        for i in nums and dul_nums:      # Check if this is the highest frequency
            if count > max_count:
                max_count = count
                Most_frequent = i

        print(f"The most frequent element is: {Most_frequent}")
        print(f"It appears {max_count} times.")


Obj = Frequencies()

nums = [1, 1, 3, 2, 4, 6, 8, 4, 6, 3, 8]

dul_nums = []

Obj.solution(nums, dul_nums)


