#BRUTE SOLUTION
def medianofsortarray(arr1, arr2, arr3):

    # First sort both arrays
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0

    # Compare both arrays
    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1

        else:
            arr3.append(arr2[j])
            j += 1

    # Add remaining elements of arr1
    while i < len(arr1):
        arr3.append(arr1[i])
        i += 1

    # Add remaining elements of arr2
    while j < len(arr2):
        arr3.append(arr2[j])
        j += 1

    print(f"THE COMBINED ARRAY IS {arr3}")

    # Find median
    n = len(arr3)

    if n % 2 == 1:
        medians = arr3[n // 2]

    else:
        medians = (arr3[n // 2 - 1] + arr3[n // 2]) / 2

    return medians


arr1 = [6, 4, 7, 78, 3]
arr2 = [9, 6, 3, 6, 2, 97, 65]

median = medianofsortarray(arr1, arr2, [])

print(f"THE MEDIAN OF THE ARRAYS IS {median}")


#OPTIMAL SOLUTION
def findMedianSortedArrays(arr1, arr2):

    # Always binary search the smaller array
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    m = len(arr1)
    n = len(arr2)

    left = 0
    right = m

    while left <= right:

        partition1 = (left + right) // 2

        partition2 = (m + n + 1) // 2 - partition1

        # Elements just left and right of partitions
        if partition1 == 0:
            left1 = float("-inf")
        else:
            left1 = arr1[partition1 - 1]

        if partition1 == m:
            right1 = float("inf")
        else:
            right1 = arr1[partition1]

        if partition2 == 0:
            left2 = float("-inf")
        else:
            left2 = arr2[partition2 - 1]

        if partition2 == n:
            right2 = float("inf")
        else:
            right2 = arr2[partition2]

        # Correct partition
        if left1 <= right2 and left2 <= right1:

            # Odd total length
            if (m + n) % 2 == 1:
                return max(left1, left2)

            # Even total length
            return (max(left1, left2) + min(right1, right2)) / 2

        # partition1 is too far right
        elif left1 > right2:
            right = partition1 - 1

        # partition1 is too far left
        else:
            left = partition1 + 1

    





                      
    