

class QuickSort(object):

    def quick_sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr) - 1)


    def quick_sort_helper(self, arr, first, last):

        if first < last:
            splitpoint = self.splitter(arr, first, last)

            self.quick_sort_helper(arr, first, splitpoint - 1)
            self.quick_sort_helper(arr, splitpoint + 1, last)



    def splitter(self, arr, first, last):

        pivotal = arr[first]

        leftpoint = first + 1
        rightpoint = last

        done = False

        while not done:
            while leftpoint <= rightpoint and arr[leftpoint] <= pivotal:
                leftpoint += 1

            while rightpoint >= leftpoint and arr[rightpoint] >= pivotal:
                rightpoint -= 1

            if leftpoint > rightpoint:
                done = True

            else:
                arr[leftpoint], arr[rightpoint] = arr[rightpoint], arr[leftpoint]

        arr[first], arr[rightpoint] = arr[rightpoint], arr[first]
        print("Sorting :", arr)

        return rightpoint



arr = [100, 20, 15, 30, 5, 75, 40, 50]
print("Array before Quick sort :", arr)
QuickSort().quick_sort(arr)
print("Array after Quick sort :", arr)






# -------------------
# Output
# -------------------
# Array before Quick sort : [100, 20, 15, 30, 5, 75, 40, 50]
# Sorting : [50, 20, 15, 30, 5, 75, 40, 100]
# Sorting : [40, 20, 15, 30, 5, 50, 75, 100]
# Sorting : [5, 20, 15, 30, 40, 50, 75, 100]
# Sorting : [5, 20, 15, 30, 40, 50, 75, 100]
# Sorting : [5, 15, 20, 30, 40, 50, 75, 100]
# Array after Quick sort : [5, 15, 20, 30, 40, 50, 75, 100]
