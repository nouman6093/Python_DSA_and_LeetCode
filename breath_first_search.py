class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                elif new_node.value < temp.value:
                    if temp.left is not None:
                        temp = temp.left
                    else:
                        temp.left = new_node
                        return True
                elif new_node.value > temp.value:
                    if temp.right is not None:
                        temp = temp.right
                    else:
                        temp.right = new_node
                        return True

    def contains(self, value):
        if self.root is None:
            return False
        else:
            temp = self.root
            while temp is not None:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return True
        return False    #it means that value doesn't exist

    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

t1 = BinarySearchTree()
