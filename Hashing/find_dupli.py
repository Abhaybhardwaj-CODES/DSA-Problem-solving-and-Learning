# WE WILL FIND DUPLICATE VALUES IN AN ARRAY USING SET DATA STRUCTURE BECAUSE SETS DO NOT ALLOW DUPLICATE VALUES.
def findDuplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)
nums = [1, 2, 3, 4, 5, 1, 2, 3]
print(findDuplicates(nums))  # Output: [1, 2, 3]