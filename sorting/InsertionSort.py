
arr = [100,20,15,30,5,75,40]

print(arr)

for i in range(1,len(arr)):
    valueToSort = arr[i]    
    
    j = i
    
    while j > 0 and arr[j-1] > valueToSort:
        arr[j] = arr[j-1]
        j -= 1
           
    arr[j] = valueToSort
    
    print(arr, "\t Sorted :: ", arr[j])


# -------------------
# Output
# -------------------
# [100, 20, 15, 30, 5, 75, 40]
# [20, 100, 15, 30, 5, 75, 40] 	 Sorted ::  20
# [15, 20, 100, 30, 5, 75, 40] 	 Sorted ::  15
# [15, 20, 30, 100, 5, 75, 40] 	 Sorted ::  30
# [5, 15, 20, 30, 100, 75, 40] 	 Sorted ::  5
# [5, 15, 20, 30, 75, 100, 40] 	 Sorted ::  75
# [5, 15, 20, 30, 40, 75, 100] 	 Sorted ::  40