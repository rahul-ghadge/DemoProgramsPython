


class Stack(object):

    def __init__(self):
        self.items = []


    def is_empty(self):
        return self.items == []


    def push(self, ele):
        self.items.append(ele)


    def size(self):
        return len(self.items)


    def pop(self):
        if self.is_empty():
            return 'Stack is empty'

        return self.items.pop()


    def peek(self):
        if self.is_empty():
            return 'Stack is empty'

        return self.items[self.size() - 1]


    def print_stack(self):
        for ele in self.items:
            print(ele)


stack = Stack()

print('Size :: ', stack.size())
print('Is Empty :: ', stack.is_empty())
print('Pushing (1) :: ', stack.push(1))
print('Pushing (2) :: ', stack.push(2))
print('Popping (2) :: ', stack.pop())
print('Pushing (Aryan) :: ', stack.push('Aryan'))
print('Pushing (True) :: ', stack.push(True))
print('Size :: ', stack.size())
print('Is Empty :: ', stack.is_empty())
print('******************************** ')
print(stack.print_stack())
print('******************************** ')
print('Peek :: ', stack.peek())




# -------------------
# Output
# -------------------
# Size ::  0
# Is Empty ::  True
# Pushing (1) ::  None
# Pushing (2) ::  None
# Popping (2) ::  2
# Pushing (Aryan) ::  None
# Pushing (True) ::  None
# Size ::  3
# Is Empty ::  False
# ********************************
# 1
# Aryan
# True
# None
# ********************************
# Peek ::  True
