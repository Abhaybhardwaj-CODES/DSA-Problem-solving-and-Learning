def move_zeros(arr):
    insert_pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1
    return arr
arr = [1,2,3,0,89,23,2,4,5,]
print(move_zeros(arr))