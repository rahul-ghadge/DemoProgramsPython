arr = [100,20,15,30,5,75,40]

print(arr)

for i in range(len(arr),1,-1):
    for j in range(0,i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
        
    print(arr, "\t", arr[j])
