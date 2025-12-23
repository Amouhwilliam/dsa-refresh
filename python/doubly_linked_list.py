class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

def traverseForwardAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def traverseBackwardAndPrint(tail):
    currentNode = tail
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.previous
    print("null")

def findMinValue(head):
    currentNode = head
    minValue = currentNode.data
    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next

    print(minValue)

def deleteNode(head, node):
   if head is node:
       return head.next

   current = head
   while current and current.next is not node:
       current = current.next

   if current and current.next:
       current.next = current.next.next
       current.next.previous = current

def insertNewNode(head, node, position):
    if position == 1:
        node.next = head
        return node

    current = head
    for _ in range(position - 2): # from 0 to position-1
        if current is None:
            break
        current = current.next

    node.next = current.next
    node.previous = current
    node.next.previous = node
    current.next = node
    return head


node1 = Node(5)
node2 = Node(10)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)
node6 = Node(42)

node1.next = node2
node1.previous = None
node2.next = node3
node2.previous = node1
node3.next = node4
node3.previous = node2
node4.next = node5
node4.previous = node3
node5.previous = node4

#traverseForwardAndPrint(node1)
#findMinValue(node1)
#traverseForwardAndPrint(deleteNode(node1, node1))
traverseForwardAndPrint(insertNewNode(node1, node6, 4))
traverseBackwardAndPrint(node5)


