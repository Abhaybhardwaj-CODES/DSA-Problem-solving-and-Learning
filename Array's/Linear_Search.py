def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f"THE NUMBER FOUND IS : {i}")
            return # found at index i
        else:
            return"THE NUMBER IS NOT PRESENT IN THE LIST"
arr = [1,2,3,0,89,23,2,4,5,]
target = int(input(" ENTER THE NUMBER YOU WANT TO SEARCH:  "))
print(linear_search(arr, target))
