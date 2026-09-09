class Solution:
    # Function to print the pattern of numbers
    def pattern_12(self, N):
        num = 1  # Starting number

        # Outer loop for the number of rows
        for i in range(1, N + 1):

            # Inner loop to print numbers increasing by 1 in each row
            for j in range(1, i + 1):
                print(num, end=" ")  # Print the current number followed by a space
                num += 1  # Increment the number for the next print

            # Move to the next line after printing the current row
            print() 

# Driver code
sol = Solution()
N = 5  # Set the size of the pattern (5 rows)
sol.pattern_12(N)