

class SumOfDigits(object):

    @staticmethod
    def sum(num):
        if num == 0:
            return 0

        all_but_last, last = num // 10, num % 10
        return sum(all_but_last) + last

        # return (num % 10) + sum(num // 10)
        # return num and (num % 10) + sum(num // 10)



print('Sum of numbers from Array :: ', SumOfDigits.sum(12345))
print('Sum of numbers from Array :: ', SumOfDigits.sum(7733))
