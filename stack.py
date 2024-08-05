class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def display(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):  #same as prepend in linked list
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height += 1
            return True
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1
            return True

    def pop(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            temp = self.top
            self.top = None
            self.height -= 1
            return temp.value
        else:
            temp = self.top
            after = self.top.next
            self.top = after
            temp.next = None
            self.height -= 1
            return temp.value

s1 = Stack(1)
