

class BinaryTree(object):

    def __init__(self, node):
        self.val = node
        self.leftNode = None
        self.rightNode = None

    def addLeftNode(self, newNode):

        if self.leftNode is None:
            self.leftNode = BinaryTree(newNode)
        else:
            node = BinaryTree(newNode)
            node.leftNode = self.leftNode
            self.leftNode = node

    def addRightNode(self, newNode):

        if self.rightNode is None:
            self.rightNode = BinaryTree(newNode)
        else:
            node = BinaryTree(newNode)
            node.rightNode = self.rightNode
            self.rightNode = node

    def getLeftChild(self):
        return self.leftNode

    def getRightChild(self):
        return self.rightNode

    def setRootValue(self, val):
        self.val = val

    def getRootValue(self):
        return self.val

root = BinaryTree(5)

root.leftNode = BinaryTree(3)
root.rightNode = BinaryTree(7)

root.leftNode.leftNode = BinaryTree(2)
root.leftNode.rightNode = BinaryTree(4)

root.rightNode.leftNode = BinaryTree(6)
root.rightNode.rightNode = BinaryTree(8)


print("Root :", root.val)
print("Root -> Left -> Left :", root.getLeftChild().getLeftChild().getRootValue())
print("Root -> Left -> Right :", root.getLeftChild().getRightChild().getRootValue())
print("Root -> Right -> Left :", root.getRightChild().getLeftChild().getRootValue())
print("Root -> Right -> Right :", root.getRightChild().getRightChild().getRootValue())







# -------------------
# Output
# -------------------
# Root : 5
# Root -> Left -> Left : 2
# Root -> Left -> Right : 4
# Root -> Right -> Left : 6
# Root -> Right -> Right : 8
