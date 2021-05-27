# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# First thoughts: Two solutions immediately come to mind, one is if the list is naively implemented
# The other is if it's not. Assuming it's not naively implemented, we should know how many nodes exist
# in the list. Otherwise we'd need to go through the entire list to know how long the list is 
# (that has it's own issues)

# For this implementation I'm going to assume that it's not naively implemented

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def printNextValue(self):
        print(self.next.value)

class LinkedList:

    def __init__(self):
        self.head = None
        self.numNodes = 0

    def printLinkedList(self):

        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next

    def addNodeAtHead(self, value):
        newHead = Node(value)
        newHead.next = self.head
        self.head = newHead
        self.numNodes += 1

    def deleteNode(self, key):

        current = self.head

        # Delete the Head node if it has the value
        if(current.value == key):
            self.head = current.next
            current = None
            return
        
        # If not the head node find the node
        while(current is not None):
            if(current.value == key):
                break
            prev = current
            current = current.next

        if(current == None):
            return

        prev.next = current.next
        current = None

    def returnKthToLast(self, k):
        current = self.head
        for _ in range(0, self.numNodes - k):

            current = current.next

        return current.value


if __name__ == "__main__":
    newList = LinkedList()

    for i in range(0,4):
        newList.addNodeAtHead(i)

    newList.printLinkedList()
    print(newList.returnKthToLast(4))