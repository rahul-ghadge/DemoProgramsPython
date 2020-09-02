

class FibonacciSeries(object):

    def fibonacci(self, num):

        # This line will print Fibonacci from 1 (not from 0)
        # if num == 0 or num == 1:
        #     return 1

        # This line will print Fibonacci from 0
        if num <= 0:
            return 0
        elif num <= 2:
            return 1
        else:
            return self.fibonacci(num - 1) + self.fibonacci(num - 2)


obj = FibonacciSeries()

num = int(input("Enter num to calculate Fibonacci series:"))

if num:
    for i in range(num):
        print("Fibonacci for ",(i + 1), "is:", obj.fibonacci(i))






# -------------------
# Output
# -------------------
# Enter num to calculate Fibonacci series:16
# Fibonacci for  1 is: 0
# Fibonacci for  2 is: 1
# Fibonacci for  3 is: 1
# Fibonacci for  4 is: 2
# Fibonacci for  5 is: 3
# Fibonacci for  6 is: 5
# Fibonacci for  7 is: 8
# Fibonacci for  8 is: 13
# Fibonacci for  9 is: 21
# Fibonacci for  10 is: 34
# Fibonacci for  11 is: 55
# Fibonacci for  12 is: 89
# Fibonacci for  13 is: 144
# Fibonacci for  14 is: 233
# Fibonacci for  15 is: 377
# Fibonacci for  16 is: 610
