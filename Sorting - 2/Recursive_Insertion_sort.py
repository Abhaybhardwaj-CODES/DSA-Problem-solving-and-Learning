def insertion_sort(arr, n):

    # Base case
    if n <= 1:
        return

    # Sort first n-1 elements
    insertion_sort(arr, n - 1)

    # Take the last element
    key = arr[n - 1]

    j = n - 2

    # Move bigger elements one position right
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Put key in correct position
    arr[j + 1] = key


arr = [7, 3, 8, 2, 6]

insertion_sort(arr, len(arr))

print(arr)