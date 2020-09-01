

class DetectLoopInLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None


    def detectLoop(self, head):

        marker1 = head
        marker2 = head

        while marker2 != None and marker2.nextNode != None:
            marker1 = marker1.nextNode
            marker2 = marker2.nextNode.nextNode

            if marker1 == marker2:
                return marker1

        return False

    def __str__(self):
        return self.value


loopedList = DetectLoopInLinkedList('head')
loopedList.nextNode = DetectLoopInLinkedList('a')
loopedList.nextNode.nextNode = DetectLoopInLinkedList('b')
loopedList.nextNode.nextNode.nextNode = DetectLoopInLinkedList('c')
loopedList.nextNode.nextNode.nextNode.nextNode = loopedList

print('Loop in Linked List :: ', loopedList.detectLoop(loopedList))


loopedList = DetectLoopInLinkedList('head')
loopedList.nextNode = DetectLoopInLinkedList('a')
loopedList.nextNode.nextNode = DetectLoopInLinkedList('b')
loopedList.nextNode.nextNode.nextNode = DetectLoopInLinkedList('c')

print('Loop in Linked List :: ', loopedList.detectLoop(loopedList))





# -------------------
# Output
# -------------------
# Loop in Linked List ::  head
# Loop in Linked List ::  False
