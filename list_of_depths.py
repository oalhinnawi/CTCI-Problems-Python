# 4.3 - List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# First thoughts: I'm going to assume I only have the root, and I'm assuming this is singularly linked

class Leaf:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def addNodeAtHead(self, value):
        newHead = Leaf(value)
        newHead.next = self.head
        self.head = newHead
        self.numNodes += 1

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree:
    
    def __init__(self):
        print("Creating Tree")

        self.root = None


    def insertNode(self, value):
        
        currentNode = None

        if(self.root == None):
            self.root = Node(value)
            return
        else:
            currentNode = self.root


        inserted = False
        while inserted is False:
            if(value < currentNode.value):
                if(currentNode.left == None):
                    currentNode.left = Node(value)
                    inserted = True
                else:
                    currentNode = currentNode.left

            elif(value >= currentNode.value):
                if(currentNode.right == None):
                    currentNode.right = Node(value)
                    inserted = True
                else:
                    currentNode = currentNode.right
    

    def createLinkedList(self):
        
        print("A")

if __name__ == "__main__":

    sortedArray = [1,2,3,4,5,6,7,8]
    BST = BinarySearchTree()
    for value in sortedArray:
        BST.insertNode(value)
