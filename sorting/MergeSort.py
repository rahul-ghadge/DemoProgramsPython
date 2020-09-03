

class MergeSort(object):

    def merge_sort(self, arr):

        if len(arr) > 1:
            mid = len(arr) // 2

            lefthalf = arr[:mid]
            righthalf = arr[mid:]

            self.merge_sort(lefthalf)
            self.merge_sort(righthalf)

            i = 0
            j = 0
            k = 0

            while i < len(lefthalf) and j < len(righthalf):

                if lefthalf[i] <= righthalf[j]:
                    arr[k] = lefthalf[i]
                    i += 1

                else:
                    arr[k] = righthalf[j]
                    j += 1

                k += 1

            while i < len(lefthalf):
                arr[k] = lefthalf[i]
                i += 1
                k += 1

            while j < len(righthalf):
                arr[k] = righthalf[j]
                j += 1
                k += 1

        print("Sorting :", arr)



arr = [100, 20, 15, 30, 5, 75, 40, 50]
print("Array before Merge sort :", arr)
MergeSort().merge_sort(arr)
print("Array after Merge sort :", arr)




# -------------------
# Output
# -------------------
# Array before Merge sort : [100, 20, 15, 30, 5, 75, 40, 50]
# Sorting : [100]
# Sorting : [20]
# Sorting : [20, 100]
# Sorting : [15]
# Sorting : [30]
# Sorting : [15, 30]
# Sorting : [15, 20, 30, 100]
# Sorting : [5]
# Sorting : [75]
# Sorting : [5, 75]
# Sorting : [40]
# Sorting : [50]
# Sorting : [40, 50]
# Sorting : [5, 40, 50, 75]
# Sorting : [5, 15, 20, 30, 40, 50, 75, 100]
# Array after Merge sort : [5, 15, 20, 30, 40, 50, 75, 100]
