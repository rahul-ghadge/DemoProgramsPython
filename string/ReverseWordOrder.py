

class ReverseWordOrder(object):

    @staticmethod
    def reverse1(str):
        return " ".join(reversed(str.split()))

    @staticmethod
    def reverse2(str):
        return " ".join(str.split()[::-1])


print(ReverseWordOrder.reverse1("best answer"))
print(ReverseWordOrder.reverse2("best answer"))



# -------------------
# Output
# -------------------
# answer best
# answer best
