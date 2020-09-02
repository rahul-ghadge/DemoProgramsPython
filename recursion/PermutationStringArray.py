

class PermutationStringArray(object):

    def permute(self, string):

        output = []
        if len(string) == 1:
            output = [string]

        else:
            for i, ch in enumerate(string):
                for param in self.permute(string[:i] + string[i + 1:]):

                    output += [ch + param]

        return output


obj = PermutationStringArray()

print("Permutation of String :: abc is ", obj.permute("abc"))
print("Permutation of String :: 1234 is ", obj.permute("1234"))







# -------------------
# Output
# -------------------
# Permutation of String :: abc is  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# Permutation of String :: 1234 is  ['1234', '1243', '1324', '1342', '1423', '1432', '2134', '2143', '2314', '2341', '2413', '2431', '3124', '3142', '3214', '3241', '3412', '3421', '4123', '4132', '4213', '4231', '4312', '4321']
