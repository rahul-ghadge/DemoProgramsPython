
class MissingFromArray(object):

    @staticmethod
    def find_missing(arr1, arr2):
        arr1.sort()
        arr2.sort()
        for num1, num2 in zip(arr1, arr2):
            if num1 != num2:
                return num1;
        return

    # def find_missing_XOR(self,arr1, arr2):
    #
    #     result = 0
    #
    #     # Performing XOR on array elements
    #     for num in arr2 + arr2:
    #         result ^= num
    #         # print(result)
    #
    #     return result



arr1 = [1, 4, 2, 6, 5, 3]
arr2 = [1, 2, 3, 4, 5, 6]
print('Missing element :: ', MissingFromArray.find_missing(arr1, arr2))

arr1 = [1, 4, 2, 7, 5, 3]
arr2 = [1, 2, 3, 4, 5, 6]
print('Missing element :: ', MissingFromArray.find_missing(arr1, arr2))


# print('*****************************************************')
# arr1 = [1, 4, 2, 6, 5, 3]
# arr2 = [1, 2, 3, 4, 5, 6]
# print('Missing element (XOR) :: ', missingfromarray.find_missing_XOR(arr1, arr2))
#
# arr1 = [1, 4, 2, 7, 5, 3]
# arr2 = [1, 2, 3, 4, 5, 6]
# print('Missing element (XOR) :: ', missingfromarray.find_missing_XOR(arr1, arr2))




# -------------------
# Output
# -------------------
# Missing element ::  None
# Missing element ::  7
