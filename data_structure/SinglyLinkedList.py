

class SinglyLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None

    @staticmethod
    def print_list(head):

        while head:
            if head.nextNode == None:
                print(head.value)
            else:
                print(head.value, end=' -> ')

            head = head.nextNode



head = SinglyLinkedList('head')
head.nextNode = SinglyLinkedList('a')
head.nextNode.nextNode = SinglyLinkedList('b')
head.nextNode.nextNode.nextNode = SinglyLinkedList('c')

SinglyLinkedList.print_list(head)




# -------------------
# Output
# -------------------
# head -> a -> b -> c
