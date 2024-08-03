class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def display(self):
        if self.length == 0:    #when there is no element:
            return None
        elif self.length == 1:  #when there is 1 element
            print(self.head.value)
        else:   #when there are more than 1 elements
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def append(self, value):    #returns True/False
        new_node = Node(value)
        if self.length == 0: #when there is no element
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True
        else:   #when there are 1 or more than 1 elements
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return True

    def pop(self):  #returns temp or temp.value or None
        if self.length == 0: #when there is no element
            return None
        elif self.length == 1: #when there is 1 element
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else: #when there are more than 1 elements
            temp = self.head
            pre = None
            while temp is not None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):   #returns True/False
        new_node = Node(value)
        if self.length == 0:    #when there is no element
            self.head = self.tail = new_node
            self.length += 1
            return True
        else:   #when there are multiple elements
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return True

    def pop_first(self):    #returns temp or temp.value or None
        if self.length == 0:    #when there is no element
            return None
        elif self.length == 1:  #when there is 1 element
            temp = self.head
            self.head = self.tail = None
            self.length -= 1
            return temp
        else:   #when there are more than 1 elements
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp

    def get_node(self, index):  #returns temp or temp.value or None
        if self.length == 0:    #when there are no elements
            return None
        elif self.length == 1:  #when there is 1 element
            if index < 0 or index >= self.length:   #when user enters wrong index
                return None
            else:   #user enters correct index
                return self.head
        else:   #when there are more than 1 elements
            if index < 0 or index >= self.length:   #when user enters wrong index
                return None
            else:   #when user enters correct index
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                return temp

    def set_value(self, index, value):  #returns True/False
        temp = self.get_node(index)
        if temp is None:    #when temp is None
            return False
        else:   #temp is not None
            temp.value = value
            return True


    def insert(self, index, value): #returns True/False
        new_node = Node(value)
        if self.length == 0:    #when there is no element
            return False
        elif index < 0 or index > self.length:    #when user enters wrong index
            return False
        elif index == 0:    #when there is only 1 element
            self.prepend(value)
            return True
        else:   #when there are more than 1 elements
            pre = self.get_node(index - 1)
            if pre is None: #when pre is None
                return False
            else:   #when pre is not None
                new_node.next = pre.next
                pre.next = new_node
                self.length += 1
                return True

    def remove(self, index):
        if index < 0 or index >= self.length:   #checking if index is out of bounds
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            pre = self.get_node(index - 1)
            if pre is None:
                return None
            else:
                temp = pre.next
                pre.next = temp.next
                temp.next = None
                self.length -= 1
                return temp

    def reverse(self):  #returns temp or temp.value or None
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp
            after = temp.next
            before = None
            for _ in range(self.length):
                after = temp.next
                temp.next = before
                before = temp
                temp = after


l1 = LinkedList(1)
