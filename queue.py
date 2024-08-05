class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def display(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):   #same as append in linked list
        new_node = Node(value)
        if self.length == 0:
            self.first = self.last = new_node
            self.length += 1
            return True
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return True


    def dequeue(self):  #same as pop_first() in linked list
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.first
            self.first = self.last = None
            self.length -= 1
            return temp.value
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -= 1
            return temp.value

d1 = Queue(1)
