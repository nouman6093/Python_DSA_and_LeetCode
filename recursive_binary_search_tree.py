class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __recursive_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__recursive_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__recursive_insert(current_node.right, value)
        return current_node


    def recursive_insert(self, value):
        if self.root == None:
            self.root = None(value)
        self.__recursive_insert(self.root, value)

    def __recursive_contains(self, current_node ,value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__recursive_contains(current_node.left, value)
        if value > current_node.value:
            return self.__recursive_contains(current_node.right, value)

    def recursive_contains(self, value):
        return self.__recursive_contains(self.root, value)

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.va

    def __delete_node(self, current_node, value):
        if current_node == None:    #if value is not in BST
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:   #if value is in BST
            if current_node.left == None and current_node.right == None:    #checks if current node is leaf node or not
                return None
            elif current_node.left == None: #checks if there is no child on the left side
                current_node = current_node.right
            elif current_node.right == None:    #checks if there is no chilc on the right side
                current_node = current_node.left
            else:   #checks if there is a child on both side
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min   #changes current_node.value to its minimum sub_tree value
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
            return current_node

    def delete_node(self, value):
        self.__delete_node(self.root, value)

t1 = BinarySearchTree()
