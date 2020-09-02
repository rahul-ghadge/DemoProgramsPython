

class BiggestInArray(object):

    def findBiggest(self, arr):

        if len(arr) == 1:
            return arr[0]
        else:
            return max(arr[0], self.findBiggest(arr[1:]))


obj = BiggestInArray()

arr = [20, 4, 56, 23, 1, 46]
print('Max Number from Array :: ', obj.findBiggest(arr))

arr = [20000, 4000, 560, 23000, 1000, ]
print('Max Number from Array :: ', obj.findBiggest(arr))




# -------------------
# Output
# -------------------
# Max Number from Array ::  56
# Max Number from Array ::  23000
