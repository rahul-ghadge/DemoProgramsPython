def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input('Enter number: '))
fact = factorial(num)
print('Factorial of',num, 'is',fact)

# -------------------
# Output
# -------------------
# Enter number:  5
# Factorial of 5 is 120
