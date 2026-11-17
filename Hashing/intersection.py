# Intersection of Two Arrays
def intersection(arr1, arr2):
    s = set(arr1)
    result = set()

    for num in arr2:

        if num in s:
            result.add(num)

    return list(result)


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

print(intersection(arr1, arr2))
