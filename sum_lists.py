# 2.5  - Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.

# First thoughts: This isn't too bad since it's in reversed order, we can construct 
# the strings as we iterate through the list, so nothing should be 2n's worth of work.

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

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
    def returnKthElement(self, k):
        current = self.head
        for _ in range(0, k - 1):

            current = current.next

        return current.value

def sumLists(firstList, secondList):

    firstSum = ""
    secondSum = ""

    # Construct the first sum
    current = firstList.head
    while current is not None:
        firstSum = str(current.value) + firstSum
        current = current.next

    # Construct the second sum
    current = secondList.head
    while current is not None:
        secondSum = str(current.value) + secondSum
        current = current.next
    firstSum = int(firstSum)
    secondSum = int(secondSum)
    print("First Sum:", firstSum)
    print("Second Sum:", secondSum)

    combinedSum = firstSum + secondSum
    combinedSum = str(combinedSum)
    print("Combined Sum:", combinedSum)
    combinedList = LinkedList()
    for num in combinedSum:
        combinedList.addNodeAtHead(int(num))
    
    return combinedList
        


if __name__ == "__main__":

    firstList = LinkedList()
    secondList = LinkedList()
    for i in range(0,4):
        firstList.addNodeAtHead(i)

    for i in range(4,10):
        secondList.addNodeAtHead(i)

    combinedList = sumLists(firstList, secondList)
    combinedList.printLinkedList()