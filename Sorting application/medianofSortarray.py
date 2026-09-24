#BRUTE SOLUTION
def medianofsortarray(arr1 , arr2 , arr3 , medians):
    for i in range (len(arr1)):
        for j in range (len(arr2)):
            if arr1[i] > arr2[j]:
                arr1[i] , arr2[j] = arr2[j] , arr1[i]
                arr3.append(arr2[i])
                i += 1
            else:
                arr3.append(arr1[j]) 
                j += 1
    print(f"THE COMBINED ARRAY IS {arr3}")      
   
    for k in range (len(arr3)):
        sum = arr3[k] + arr3 [k+1]
        k =+ 1
    medians = sum/2
print (f"THE MEDIAN OF THE ARRAY'S ARE  {medians}")

arr1 = [6,4,7,78,3]
arr2 = [9,6,3,6,2,97,65]
    


    





                      
    