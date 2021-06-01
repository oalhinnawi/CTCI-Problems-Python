# 4.2 - Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.

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
    

if __name__ == "__main__":

    sortedArray = [1,2,3,4,5,6,7,8]
    BST = BinarySearchTree()
    for value in sortedArray:
        BST.insertNode(value)



