

class largest_continue_sum(object):

    def calculate_sum(self, arr):

        if len(arr) == 0:
            return 0

        max_sum = sum = arr[0]

        for num in arr[1:]:
            sum = max(sum + num, num)
            max_sum = max(sum, max_sum)

        return max_sum

obj = largest_continue_sum()

print("Sum :: ", (obj.calculate_sum([1, 5, 3, 12, 44, -5, 2])))
print("Sum :: ", (obj.calculate_sum([1, 5, 3, -12, 44, 6, -2])))



# -------------------
# Output
# -------------------
# Sum ::  65
# Sum ::  50