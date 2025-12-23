class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListQueue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "the queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "the queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return not self.queue

    def size(self):
        return len(self.queue)

class LinkedListQueue:

    def __init__(self):
         self.head = None
         self.tail = None
         self.size = 0

    def enqueue(self, item): # pushing behind the tail (ie. tail.next = None)
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self): # removing the head(ie. head.next = some node)
        if self.isEmpty():
           return "Queue is empty"
        temp = self.head
        self.head = temp.next
        self.size -= 1
        if self.head is None:
            self.tail = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.head.data

    def isEmpty(self):
        return self.size == 0

    def length(self):
        print(self.size)

    def printQueue(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")


queue = LinkedListQueue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

queue.length()

queue.printQueue()
