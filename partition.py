# 2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.

# First thoughts: There are a few ways of going about this one, my immediate thought is to do two passes through the list
# First pass would find anything bigger than the partition and insert that into the head node first

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

# Naive partitioning
def partitionLinkedList(partition, unpartitionedList):

    value = unpartitionedList.returnKthElement(partition)
    print("Partitiuon Value: ", value)
    # Create new list to be our buffer
    partitionedList = LinkedList()

    # Iterate through each Node in the unpartitioned list
    

    # First pass will get any values that are more than the partition, then insert them into the new list
    currentNode = unpartitionedList.head
    while currentNode is not None:
        if(currentNode.value > value):
            partitionedList.addNodeAtHead(currentNode.value)
        currentNode = currentNode.next

    # Second pass will get any values equal than the partition
    currentNode = unpartitionedList.head
    while currentNode is not None:
        if(currentNode.value == value):
            partitionedList.addNodeAtHead(currentNode.value)
        currentNode = currentNode.next
    

    # Second pass will get any values equal than the partition
    currentNode = unpartitionedList.head
    while currentNode is not None:
        if(currentNode.value < value):
            partitionedList.addNodeAtHead(currentNode.value)
        currentNode = currentNode.next
    return partitionedList


if __name__ == "__main__":
    newList = LinkedList()

    for i in range(0,4):
        newList.addNodeAtHead(i)

    for i in range(0,4):
        newList.addNodeAtHead(i)

    print("Before Partition")
    newList.printLinkedList()
    print("Beginning Partition")
    
    partitionedList = partitionLinkedList(3, newList)
    print("After Partition")
    partitionedList.printLinkedList()
