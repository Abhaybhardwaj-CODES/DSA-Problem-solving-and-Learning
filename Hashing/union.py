#  UNION OF TWO ARRAYS
def union(arr1, arr2):
    # Create a set to store unique elements
    unique_elements = set()

    # Add elements from the first array to the set
    for num in arr1:
        unique_elements.add(num)

    # Add elements from the second array to the set
    for num in arr2:
        unique_elements.add(num)

    # Convert the set back to a list and return it
    return list(unique_elements)

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]  
print(union(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]    