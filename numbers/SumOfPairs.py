


class SumOfPairs(object):

    @staticmethod
    def pairs_count(array, num):

        if len(array) <= 2:
            return

        visited = set()
        output = set()


        for n in array:
            target = num - n

            if target not in visited:
                visited.add(target)

            else:
                output.add( (min(n, target), max(n, target) ))


        print("Found :: ", output)
        return len(output)


print('Number of pairs :: ', SumOfPairs.pairs_count([1, 1, 3, 2, 4, 2], 4))


# -------------------
# Output
# -------------------
# Found ::  {(1, 3), (2, 2)}
# Number of pairs ::  2


