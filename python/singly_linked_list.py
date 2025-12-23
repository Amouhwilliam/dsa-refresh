class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
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

def insertNewNode(head, node, position):
    if position is 1:
        node.next = head
        return node

    current = head
    for _ in range(position - 2): # from 0 to position-1
        if current is None:
            break
        current = current.next

    node.next = current.next
    current.next = node
    return head


node1 = Node(5)
node2 = Node(10)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)
node6 = Node(42)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
findMinValue(node1)
traverseAndPrint(deleteNode(node1, node1))
traverseAndPrint(insertNewNode(node1, node6, 3))


