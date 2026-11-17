# Count Distinct Values in an Array
""" WE WILL USE SET DATA STRUCTURE TO COUNT DISTINCT VALUES IN AN ARRAY BECAUSE SETS DO NOT ALLOW DUPLICATE VALUES. """
def countDistinctValues(arr):
    return len(set(arr))
arr = [1, 2, 3, 4, 5, 1, 2, 3]
print(countDistinctValues(arr))  # Output: 5