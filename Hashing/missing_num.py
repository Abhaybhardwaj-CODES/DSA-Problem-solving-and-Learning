# using set to find the missing number in an array
def find_missing_number(arr, n):
    # Create a set of numbers from 1 to n
    num_set = set(range(1, n + 1))
    
    # Remove the numbers present in the array from the set
    for num in arr:
        if num in num_set:
            num_set.remove(num)
    
    # The remaining number in the set is the missing number
    return num_set.pop() if num_set else None
arr = [1, 2, 4, 5, 6]
n = 6
print(find_missing_number(arr, n))  # Output: 3