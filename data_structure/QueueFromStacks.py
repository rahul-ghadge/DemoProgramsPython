

class QueueFromStacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []


    def enqueue(self, item):
        self.instack.append(item)


    def dequeue(self):

        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


queue = QueueFromStacks()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())



# -------------------
# Output
# -------------------
# 10
# 20
# 30