# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

# First Thoughts: Occam's Razor comes to mind, could we just construct a string and check that? 
# On second thought that would probably defeat the purpose of this 
# Third thought: I realized now that this probably needs to utilize something like the runner technique
# In other words, we'll need a doubly linked list for this problem. (I know it's not called runner)

import math

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.numNodes = 0

    def printLinkedList(self):

        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
            

    def addNodeAtHead(self, value):
        
        newHead = Node(value)
        newHead.next = self.head
        if(self.head is not None):
            self.head.prev = newHead
        self.head = newHead
        if(self.head.next == None):
            self.tail = self.head


        self.numNodes += 1

    def returnKthElement(self, k):
        current = self.head
        for _ in range(0, k - 1):

            current = current.next

        return current.value

    def isPalindrome(self):

        currentHead = self.head
        currentTail = self.tail
        midPoint = math.ceil(self.numNodes/2)
        for i in range(0, midPoint):
            if currentHead.value == currentTail.value:
                currentHead = currentHead.next
                currentTail = currentTail.prev
            else:
                return False

        return True

if __name__ == "__main__":
    newList = LinkedList()
    length = 10
    for i in range(0, length):
        newList.addNodeAtHead(i)
    for i in range(length - 1, -1, -1):
        newList.addNodeAtHead(i)
    newList.printLinkedList()
    print(newList.isPalindrome())