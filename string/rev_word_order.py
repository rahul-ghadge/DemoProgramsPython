

class rev_word_order(object):

    def reverse1(self, str):
        return " ".join(reversed(str.split()))

    def reverse2(self, str):
        return " ".join(str.split()[::-1])


obj = rev_word_order()
print(obj.reverse1("best answer"))
print(obj.reverse2("best answer"))



# -------------------
# Output
# -------------------
# answer best
# answer best
