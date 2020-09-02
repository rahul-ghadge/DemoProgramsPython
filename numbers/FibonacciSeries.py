

class FibonacciSeries(object):

    def fibonacci(self, num):

        a, b = 0, 1

        for i in range(num):
            a,b = b, a+b

        return a


obj = FibonacciSeries()

print("Fibonacci of 10 is:",obj.fibonacci(10))




# -------------------
# Output
# -------------------
# Fibonacci of 10 is: 55
