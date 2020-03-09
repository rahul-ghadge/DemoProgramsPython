def linearSearch(arr, value):
    position = 0
    found = False
    while position < len(arr) and not found:
        if arr[position] == value:
            found = True
        else:
            position = position + 1
    
    return found

arr = [10, 20, 30, 40, 50]

value = 35
found = linearSearch(arr, value)
print('Value found:', found)

value = 20
found = linearSearch(arr, value)
print('Value found:', found)

# -------------------
# Output
# -------------------
# Value found: False
# Value found: True
