
arr = [100,20,15,30,5,75,40]

print(arr)

for i in range(1,len(arr)):
    valueToSort = arr[i]    
    
    j = i
    
    while j > 0 and arr[j-1] > valueToSort:
        arr[j] = arr[j-1]
        j -= 1
           
    arr[j] = valueToSort
    
    print(arr, "\t", arr[j])

