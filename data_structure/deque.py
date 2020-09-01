

class deque(object):

    def __init__(self):
        self.items = []


    def isempty(self):
        return self.items == []


    def add_front(self, item):
        self.items.append(item)


    def add_rear(self, item):
        self.items.insert(0, item)


    def remove_front(self):
        return self.items.pop()


    def remove_rear(self):
        return self.items.pop(0)


    def size(self):
        return len(self.items)


    def print_stack(self):
        for item in self.items:
            print(item)



deque = deque()

print('Size :: ', deque.size())
print('Is Empty :: ', deque.isempty())
print('Add Front (1) :: ', deque.add_front(1))
print('Add Rear (2) :: ', deque.add_rear(2))
print('Remove Front (1) :: ', deque.remove_front())
print('Remove Rear (2) :: ', deque.remove_rear())
print('Add Front (Aryan) :: ', deque.add_front('Aryan'))
print('Add Rear (True) :: ', deque.add_rear(True))
print('Size :: ', deque.size())
print('Is Empty :: ', deque.isempty())
print('******************************** ')
print(deque.print_stack())



# -------------------
# Output
# -------------------
# Size ::  0
# Is Empty ::  True
# Add Front (1) ::  None
# Add Rear (2) ::  None
# Remove Front (1) ::  1
# Remove Rear (2) ::  2
# Add Front (Aryan) ::  None
# Add Rear (True) ::  None
# Size ::  2
# Is Empty ::  False
# ********************************
# True
# Aryan
# None