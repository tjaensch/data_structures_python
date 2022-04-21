class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def minimum(self):
        temp = self.root
        while temp.left is not None:
            temp = temp.left
        return temp

    def maximum(self):
        temp = self.root
        while temp.right is not None:
            temp = temp.right
        return temp

    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def max_value_node(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node

def addBT(root):  
    if (root == None): 
        return 0
    return (root.value + addBT(root.left) + 
                       addBT(root.right))  
            
        
bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(10)
bst.insert(3)
bst.insert(4)

print(addBT(bst.root))


    