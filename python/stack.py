class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListStack:

     def __init__(self):
         self.stack = []

     def push(self, item):
         self.stack.append(item)

     def pop(self):
         if self.isEmpty():
            return "Stack is empty"
         return self.stack.pop()

     def peek(self):
         if self.isEmpty():
             return "Stack is empty"
         return self.stack[-1]

     def isEmpty(self):
         return not self.queue

class LinkedListStack:

     def __init__(self):
         self.head = None
         self.size = 0

     def push(self, item):
         new_node = Node(item)
         if self.head:
            new_node.next = self.head
         self.head = new_node
         self.size += 1

     def pop(self):
         if self.isEmpty():
            return "Stack is empty"

         popped_node = self.head
         self.head = self.head.next
         self.size -= 1
         return popped_node.data

     def peek(self):
         if self.isEmpty():
             return "Stack is empty"
         return self.head.data

     def isEmpty(self):
         return self.size == 0

     def traverseAndPrint(self):
         current = self.head
         while current:
             print(current.data, end=" -> ")
             current = current.next
         print("null")


stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.traverseAndPrint())