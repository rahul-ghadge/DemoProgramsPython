


class Queue(object):

    def __init__(self):
        self.items = []


    def isempty(self):
        return self.items == []


    def enqueue(self, ele):
        self.items.insert(0, ele)


    def dequeue(self):
        self.items.pop()


    def size(self):
        return len(self.items)


    def print_stack(self):
        for ele in self.items:
            print(ele)


queue = Queue()

print('Size :: ', queue.size())
print('Is Empty :: ', queue.isempty())
print('Enqueue (1) :: ', queue.enqueue(1))
print('Enqueue (2) :: ', queue.enqueue(2))
print('Dequeue (1) :: ', queue.dequeue())
print('Enqueue (Aryan) :: ', queue.enqueue('Aryan'))
print('Enqueue (True) :: ', queue.enqueue(True))
print('Size :: ', queue.size())
print('Is Empty :: ', queue.isempty())
print('******************************** ')
print(queue.print_stack())



# -------------------
# Output
# -------------------
# Size ::  0
# Is Empty ::  True
# Enqueue (1) ::  None
# Enqueue (2) ::  None
# Dequeue (1) ::  None
# Enqueue (Aryan) ::  None
# Enqueue (True) ::  None
# Size ::  3
# Is Empty ::  False
# ********************************
# True
# Aryan
# 2
# None