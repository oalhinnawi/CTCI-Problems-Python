# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.

# First Thoughts: I'm going ot assume that the LinkedList class is banned for use here, because then this
# Would be too easy, so to construct my toy problem I'm going to construct a chain of Nodes so that we have
# something to work with. I'm also going to assume that it doesn't matter what actually came before the
# middle Node. If we're already given the middle Node, all we really need to do is move the rest of the
# chained nodes up and set the last ones nextNode equal to None (easier said than done)

import math

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


# def deleteMiddleNode(midNode):



if __name__ == "__main__":
    currentNode = Node(0)
    head = currentNode

    length = 7
    for i in range(1,length):
        currentNode.next = Node(i)
        currentNode = currentNode.next

    # Print out the List
    currentNode = head
    while(currentNode is not None):
        print(currentNode.value)
        currentNode = currentNode.next
    print("+==============================+")
    
    # Go to the middle node
    currentNode = head
    for i in range(0, math.ceil(length/2)):
        currentNode = currentNode.next

    # From the middle Node till None, move everything up one
    while currentNode is not None:
        if currentNode.next == None:
            prev.next = None
        else:
            currentNode.value = currentNode.next.value
            prev = currentNode
            currentNode = currentNode.next

    # Print out the List
    currentNode = head
    while(currentNode is not None):
        print(currentNode.value)
        currentNode = currentNode.next    
    print("+==============================+")