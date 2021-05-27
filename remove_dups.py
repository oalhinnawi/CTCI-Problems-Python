# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?

# First Thoughts: Duplicate is kind of open ended, but I'm pretty sure they mean values
# For the sake of simplicity I'm going to assume that they want this done for a singly linked list
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
    
    # def addNodeAtTail(self, value):
    #     print("A")


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

    def findDuplicates(self):
        valueDict = {}
        valuesToDelete = []
        currentNode = self.head
        while currentNode is not None:
            if(str(currentNode.value) in valueDict):
                valuesToDelete.append(currentNode.value)
            else:
                valueDict[str(currentNode.value)] = 1
            currentNode = currentNode.next
        return valuesToDelete

if __name__ == "__main__":
    newList = LinkedList()

    for i in range(0,4):
        newList.addNodeAtHead(i)
    newList.addNodeAtHead(1)
    newList.addNodeAtHead(1)

    
    newList.printLinkedList()
    print("=============================")
    duplicates = newList.findDuplicates()
    for duplicate in duplicates:
        newList.deleteNode(duplicate)
    newList.printLinkedList()