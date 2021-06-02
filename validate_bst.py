# 4.5 - Validate BST: Implement a function to check if a binary tree is a binary search tree.

# First thoughts: Ok so generally the rule of thumb goes thus: If the left is smaller than the parents,
# and the right is bigger than the parent then it should be valid, this needs to hold true for all nodes
# in the tree.

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

    # Helper function to check each individual node
    def checkNode(self, leaf):
        if(leaf == None):
            return True
         
        if not (leaf.right.value >= leaf.value or leaf.right == None):
            return False

        if not (leaf.left.value < leaf.value or leaf.left == None):
            return False

        return True



    # Primary Recursive Function
    def validateBST(self):

        self.checkNode(self.root)

        # Start from the root, and go from there.
        print("BST Valid:", )
