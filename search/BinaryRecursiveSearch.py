

def binaryRecursiveSearch(arr, value, low, high):
    
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        
        if value == arr[mid]:
            return True
        elif value < arr[mid]:
            return binaryRecursiveSearch(arr, value, low, mid - 1)
        else:
            return binaryRecursiveSearch(arr, value, mid + 1, high)


arr = [10, 20, 30, 40, 50]

value = 35
found = binaryRecursiveSearch(arr, value, 0, len(arr)-1)
print('Value found:', found)      
        
value = 20
found = binaryRecursiveSearch(arr, value, 0, len(arr)-1)
print('Value found:', found)








def binarySearchRecursive(arr, ele):

    if len(arr) == 0:
        return False

    else:

        mid = len(arr) // 2

        if arr[mid] == ele:
            return True

        else:
            if mid < arr[mid]:
                return binarySearchRecursive(arr[:mid], ele)
            else:
                return binaryRecursiveSearch(arr[mid:], ele)


print("\n***************************************************")
arr = [10, 20, 30, 40, 50]

value = 35
found = binarySearchRecursive(arr, value)
print('Value found:', found)

value = 20
found = binarySearchRecursive(arr, value)
print('Value found:', found)








# -------------------
# Output
# -------------------
# Value found: False
# Value found: True
#
# ***************************************************
# Value found: False
# Value found: True
