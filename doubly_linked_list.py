class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            self.length += 1
            return True
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True

    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
            self.length += 1
            return True
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.head.prev = None
            self.length += 1
            return True

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp.value
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            temp.prev = None
            self.head.prev = None
            self.length -= 1
            return temp.value

    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        temp = self.get_node(index)
        if index is None:
            return False
        elif index is not None:
            temp.value = value
            return True
        else:
            return False

    def insert(self, index, value):
        new_node = Node(value)
        if self.length == 0:
            return False
        elif index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            before = self.get_node(index - 1)
            after = before.next
            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node
            self.length += 1
            return True

    def remove(self, index):
        if self.length == 0:
            return None
        elif index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get_node(index)
            if temp is None:
                return None
            else:
                temp.next.pre = temp.prev
                temp.prev.next = temp.next
                temp.next = None
                temp.prev = None
                self.length -= 1
                return temp.value

d1 = DoublyLinkedList(0)
