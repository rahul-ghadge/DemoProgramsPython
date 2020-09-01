

class LargestContinueSum(object):

    @staticmethod
    def calculate_sum(arr):

        if len(arr) == 0:
            return 0

        max_sum = sum = arr[0]

        for num in arr[1:]:
            sum = max(sum + num, num)
            max_sum = max(sum, max_sum)

        return max_sum


print("Sum :: ", (LargestContinueSum.calculate_sum([1, 5, 3, 12, 44, -5, 2])))
print("Sum :: ", (LargestContinueSum.calculate_sum([1, 5, 3, -12, 44, 6, -2])))



# -------------------
# Output
# -------------------
# Sum ::  65
# Sum ::  50