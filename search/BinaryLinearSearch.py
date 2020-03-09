def binaryLinearSearch(arr, value):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if value == arr[mid]:
            return True
        elif value < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return False

arr = [10, 20, 30, 40, 50]

value = 35
found = binaryLinearSearch(arr, value)
print('Value found:', found)      
        
value = 20
found = binaryLinearSearch(arr, value)
print('Value found:', found)

# -------------------
# Output
# -------------------
# Value found: False
# Value found: True
