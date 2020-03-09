def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input('Enter number: '))
fact = factorial(num)
print(fact)

# -------------------
# Output
# -------------------
# Enter number:  5
# 120
