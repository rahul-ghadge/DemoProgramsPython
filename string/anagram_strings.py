
class anagram_strings(object):

    def is_anagram1(self, str1, str2):

        str1 = str1.replace(' ', '').lower()
        str2 = str2.replace(' ', '').lower()

        return sorted(str1) == sorted(str2)



    def is_anagram2(self, str1, str2):

        str1 = str1.replace(' ', '').lower()
        str2 = str2.replace(' ', '').lower()

        if len(str1) != len(str2):
            return False

        count = {}

        for letter in str1:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

        for letter in str2:
            if letter in count:
                count[letter] -= 1
            else:
                count[letter] = 1

        for letter in count:
            if count[letter] != 0:
                return False
            return True





anagram_strings = anagram_strings()

print("*********  Checking Anagram with function 1  ****************")
print(anagram_strings.is_anagram1("god", "dog"))
print(anagram_strings.is_anagram1("Listen", "Silent"))
print(anagram_strings.is_anagram1("eleven plus two", "twelve plus one"))

print(anagram_strings.is_anagram1("Random string", "Another String"))




print("*********  Checking Anagram with function 2  ****************")
print(anagram_strings.is_anagram2("god", "dog"))
print(anagram_strings.is_anagram2("Listen", "Silent"))
print(anagram_strings.is_anagram2("eleven plus two", "twelve plus one"))

print(anagram_strings.is_anagram2("Random string", "Another String"))



# -------------------
# Output
# -------------------
# *********  Checking Anagram with function 1  ****************
# True
# True
# True
# False
# *********  Checking Anagram with function 2  ****************
# True
# True
# True
# False
